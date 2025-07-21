import datetime
import requests
import json
import arxiv
import os
from arxiv import UnexpectedEmptyPageError
import matplotlib.pyplot as plt
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime




base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

BASE_URL = "https://arxiv.paperswithcode.com/api/v0/papers/"

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
    if len(categories) != 1:  
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

    # 1. arxiv client
    client = arxiv.Client(
        page_size=100,    
        delay_seconds=3,  
        num_retries=5    
    )

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    # 2. iter_results
    for res in iter_results_safe(client, search):

        cats = res.categories                 # e.g. ['cs.CL', 'cs.LG']
        if (KEEP not in cats) or any(c in cats for c in BLOCKS):
            continue                        

        paper_id_full  = res.get_short_id()  
        paper_id       = paper_id_full.split("v")[0]  
        update_time    = res.updated.date()
        paper_title    = res.title
        paper_url      = res.entry_id
        paper_abstract = res.summary.replace("\n", " ")
        collapsed_abs = make_collapsible(paper_abstract)      
        paper_labels   = ", ".join(cats)

        repo_url = "null"
        try:
            r = requests.get(BASE_URL + paper_id_full, timeout=10).json()
            if r.get("official"):
                repo_url = r["official"]["url"]
        except Exception as e:
            print(f"PwC lookup failed for {paper_id_full}: {e}")

        md_row = (
            f"|**{update_time}**|**{paper_title}**|{paper_labels}| "
            f"{collapsed_abs}|[{paper_id_full}]({paper_url})| "
        )
        md_row += f"**[code]({repo_url})**|" if repo_url != "null" else "null|"

        content[paper_id] = md_row

    return {topic: content}


def make_collapsible(text: str, title: str = "Full Abstract") -> str:
    text = text.replace("|", "\\|")      
    return f"<details><summary>{title}</summary>{text}</details>"

def wrap_old_row(md_row: str) -> str:
    if "<details" in md_row:
        return md_row

    newline = "\n" if md_row.endswith("\n") else ""
    row = md_row.rstrip("\n")  
    cells = row.split("|")
    if len(cells) < 8:         
        return md_row

    cells[4] = make_collapsible(cells[4].strip())

    return "|".join(cells) + newline

def update_json_file(filename, data_all):
    with open(filename, "r") as f:
        content = f.read().strip()
    json_data = json.loads(content) if content else {}

    for kw in json_data.values():
        for pid in list(kw.keys()):
            kw[pid] = wrap_old_row(kw[pid])

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

        f.write("![Monthly Trend](imgs/trend.png)\n\n")

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

            for _, v in day_content.items():
                if not v:       
                    continue
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

def json_to_trend(json_file: str | Path, img_file: str | Path) -> None:
    json_file = Path(json_file).expanduser().resolve()
    img_file  = Path(img_file).expanduser().resolve()

    with json_file.open("r", encoding="utf‑8") as f:
        data = json.load(f)

    counts = Counter()
    for topic_dict in data.values():
        for arxiv_id in topic_dict.keys():
            yymm = arxiv_id[:4]
            year  = 2000 + int(yymm[:2])
            month = int(yymm[2:])
            ym_key = f"{year:04d}-{month:02d}"
            counts[ym_key] += 1

    if not counts:
        print("no data")
        return

    ym_dates = {datetime.strptime(k, "%Y-%m"): k for k in counts}
    sorted_keys = [ym_dates[d] for d in sorted(ym_dates)]
    values = [counts[k] for k in sorted_keys]
    idx_map = {k: i for i, k in enumerate(sorted_keys)}

    year_tot, year_months = defaultdict(int), defaultdict(int)
    for k, v in counts.items():
        y = k[:4]
        year_tot[y]   += v
        year_months[y] += 1
    year_avg = {y: year_tot[y] / year_months[y] for y in year_tot}

    year_span = defaultdict(list)
    for k in sorted_keys:
        year_span[k[:4]].append(idx_map[k])

    plt.figure(figsize=(9, 4))
    plt.plot(sorted_keys, values, marker="o", linewidth=1, label="Monthly count")

    first_bar = True
    for y, avg in year_avg.items():
        xs = year_span[y]
        xmin, xmax = min(xs), max(xs)
        bar_x = (xmin + xmax) / 2
        bar_w = (xmax - xmin + 1) * 0.8    
        plt.bar(bar_x, avg,
                width=bar_w,
                color="C1",
                alpha=0.2,
                label=f"Anual avg" if first_bar else None)
        first_bar = False 

    plt.title("ArXiv Papers per Month")
    # plt.xlabel("Month")
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45, ha="right")
    plt.legend()

    img_file.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(img_file, dpi=300)
    plt.close()
    print(f"✅ trend save in: {img_file}")


if __name__ == "__main__":

    data_collector = []

    # my keyword
    keywords = dict()
    keywords["diffusion"] = "ti:\"diffusion\""  + "OR" + "ti:\" diffus\""

    for topic, keyword in keywords.items():
        print("Keyword: " + topic)

        data = get_daily_papers(topic, query=keyword, max_results=200)
        data_collector.append(data)

        print("\n")

    json_file = "docs/arxiv-daily.json"
    img_file = "imgs/trend.png"
    md_file = "README.md"

    update_json_file(json_file, data_collector)
    json_to_trend(json_file, img_file)
    json_to_md(json_file, md_file)