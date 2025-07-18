import datetime
import requests
import json
import arxiv
import os
from arxiv import UnexpectedEmptyPageError


base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

BASE_URL = "https://arxiv.paperswithcode.com/api/v0/papers/"

# 想保留的主类 & 想屏蔽的类
KEEP   = "cs.CL"
BLOCKS = {"cs.CV", "eess.AS", "cs.SD", "eess.SP", "q-bio.BM"}


def get_authors(authors, first_author=False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output


def get_label(categories):
    output = str()
    if len(categories) != 1:  # 多类
        output = ", ".join(str(c) for c in categories)
    else:
        output = categories[0]
    return output


def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output

def iter_results_safe(client, search):
    gen = client.results(search)
    while True:
        try:
            yield next(gen)
        except UnexpectedEmptyPageError as e:
            print(f"[arXiv] empty page, stop paging: {e}")
            break
        except StopIteration:
            break

def get_daily_papers(topic, query, max_results=200):
    """
    抓取 arXiv + PapersWithCode 信息并按 markdown 表格行返回
    """
    content: dict[str, str] = {}

    # 1. arxiv 客户端（新版推荐写法）
    client = arxiv.Client(
        page_size=100,     # 每页 100 条
        delay_seconds=3,   # 尊重 API 速率
        num_retries=5      # 同一页最多重试 5 次
    )

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    # 2. 逐条遍历结果
    for res in iter_results_safe(client, search):

        cats = res.categories                 # e.g. ['cs.CL', 'cs.LG']
        if (KEEP not in cats) or any(c in cats for c in BLOCKS):
            continue                          # 不符合过滤条件

        # ---- 基本字段 ----
        paper_id_full  = res.get_short_id()   # 2407.12345v1
        paper_id       = paper_id_full.split("v")[0]  # 去掉版本号
        update_time    = res.updated.date()
        paper_title    = res.title
        paper_url      = res.entry_id
        paper_abstract = res.summary.replace("\n", " ")
        collapsed_abs = make_collapsible(paper_abstract)       # ← 折叠后的摘要
        paper_labels   = ", ".join(cats)

        # ---- PapersWithCode 源码链接 ----
        repo_url = "null"
        try:
            r = requests.get(BASE_URL + paper_id_full, timeout=10).json()
            if r.get("official"):
                repo_url = r["official"]["url"]
        except Exception as e:
            print(f"PwC lookup failed for {paper_id_full}: {e}")

        # ---- 拼 markdown 行 ----
        md_row = (
            f"| **{update_time}** | **{paper_title}** | {paper_labels} | "
            f"{collapsed_abs} | [{paper_id_full}]({paper_url}) | "
        )
        md_row += f"**[code]({repo_url})** |" if repo_url != "null" else "null |"

        content[paper_id] = md_row

    return {topic: content}


def make_collapsible(text: str, title: str = "Full Abstract") -> str:
    """
    用 <details>/<summary> 包一段文本，方便在表格里折叠显示
    """
    # GitHub 会把单元格里的换行渲染成 <br>，保持可读
    text = text.replace("|", "\\|")        # 避免 ‘|’ 撑破表格
    return f"<details><summary>{title}</summary>{text}</details>"

def wrap_old_row(md_row: str) -> str:
    # 已经有 <details> 就跳过
    if "<details" in md_row:
        return md_row

    # 记录行尾是否带 '\n'
    newline = "\n" if md_row.endswith("\n") else ""
    row = md_row.rstrip("\n")  # 去掉行尾换行再处理

    # 用 split 保留首尾空串：'' , Date , Title , ... , ''  (共 7+2 节点)
    cells = row.split("|")
    if len(cells) < 8:         # 不够 8 说明行格式本身就异常
        return md_row

    # 第 4 格 = 摘要
    cells[4] = make_collapsible(cells[4].strip())

    # 重新组装，记得把首尾空格、换行补回去
    return "|".join(cells) + newline

def update_json_file(filename, data_all):
    with open(filename, "r") as f:
        content = f.read().strip()
    json_data = json.loads(content) if content else {}

    # ① 把旧行先补丁
    for kw in json_data.values():
        for pid in list(kw.keys()):
            kw[pid] = wrap_old_row(kw[pid])

    # ② 再正常合并新抓到的数据
    for data in data_all:
        for keyword, papers in data.items():
            json_data.setdefault(keyword, {}).update(papers)

    with open(filename, "w") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

def json_to_md(filename, md_filename,
               to_web=False,
               use_title=True,
               use_tc=True,
               show_badge=True):
    """
    @param filename: str
    @param md_filename: str
    @return None
    """

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-', '.')

    with open(filename, "r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    # clean README.md if daily already exist else create it
    with open(md_filename, "w+") as f:
        pass

    # write data into README.md
    with open(md_filename, "a+") as f:

        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")

        if show_badge == True:
            f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            f.write(f"[![Forks][forks-shield]][forks-url]\n")
            f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            f.write(f"[![Issues][issues-shield]][issues-url]\n\n")

        # add another code repository link
        f.write("For more carefully curated articles, you can refer to this [repository](https://github.com/bansky-cl/Diffusion_NLP_Papers).\n\n")

        if use_title == True:
            f.write("## Updated on " + DateNow + "\n\n")
        else:
            f.write("> Updated on " + DateNow + "\n\n")

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {keyword}\n\n")

            if use_title == True:
                if to_web == False:
                    f.write("|Date|Title|label|Abstract|PDF|Code|\n" + "|---|---|---|---|---|---|\n")
                else:
                    f.write("| Date | Title | label | Abstract | PDF | Code |\n")
                    f.write("|:---------|:---------------|:-------|:------------------|:------|:------|\n")

            # sort papers by date
            day_content = sort_papers(day_content)

            # for _, v in day_content.items():
            #     if v is not None:
            #         f.write(v)
            for _, v in day_content.items():
                if not v:          # 跳过空值
                    continue
                # 去掉可能已有的行尾换行，再补一个
                f.write(v.rstrip("\n") + "\n")

            f.write(f"\n")

            # Add: back to top
            top_info = f"#Updated on {DateNow}"
            top_info = top_info.replace(' ', '-').replace('.', '')
            f.write(f"<p align=right>(<a href={top_info}>back to top</a>)</p>\n\n")

        if show_badge == True:
            # unk
            f.write(
                f"[contributors-shield]: https://img.shields.io/github/contributors/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge\n")
            f.write(f"[contributors-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/graphs/contributors\n")
            f.write(
                f"[forks-shield]: https://img.shields.io/github/forks/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge\n")
            f.write(f"[forks-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/network/members\n")
            f.write(
                f"[stars-shield]: https://img.shields.io/github/stars/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge\n")
            f.write(f"[stars-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/stargazers\n")
            f.write(
                f"[issues-shield]: https://img.shields.io/github/issues/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge\n")
            f.write(f"[issues-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/issues\n\n")

    print("finished")


if __name__ == "__main__":

    data_collector = []

    # my keyword
    keywords = dict()
    keywords["diffusion"] = "ti:\"diffusion\""  + "OR" + "ti:\" diffus\""

    for topic, keyword in keywords.items():
        # topic = keyword.replace("\"","")
        print("Keyword: " + topic)

        # data 就是md格式
        # web 就是json格式
        # 这里调用 搜索函数，返回一个topic或者一个keyword符合条件的所有函数
        data = get_daily_papers(topic, query=keyword, max_results=200)
        data_collector.append(data)
        # data_collector_web.append(data_web) # no use

        print("\n")

    json_file = "docs/arxiv-daily.json"
    md_file = "README.md"

    update_json_file(json_file, data_collector)
    json_to_md(json_file, md_file)
