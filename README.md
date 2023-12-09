[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.09

## diffusion

|Date|Title|label|Abstract|PDF|Code|
|---|---|---|---|---|---|
|**2023-11-29**|**ChatTraffic: Text-to-Traffic Generation via Diffusion Model**|cs.LG, cs.AI, cs.CL|Traffic prediction is one of the most significant foundations in Intelligent Transportation Systems (ITS). Traditional traffic prediction methods rely only on historical traffic data to predict traffic trends and face two main challenges. 1) insensitivity to unusual events. 2) poor performance in long-term prediction. In this work, we explore how generative models combined with text describing the traffic system can be applied for traffic generation and name the task Text-to-Traffic Generation (TTG). The key challenge of the TTG task is how to associate text with the spatial structure of the road network and traffic data for generating traffic situations. To this end, we propose ChatTraffic, the first diffusion model for text-to-traffic generation. To guarantee the consistency between synthetic and real data, we augment a diffusion model with the Graph Convolutional Network (GCN) to extract spatial correlations of traffic data. In addition, we construct a large dataset containing text-traffic pairs for the TTG task. We benchmarked our model qualitatively and quantitatively on the released dataset. The experimental results indicate that ChatTraffic can generate realistic traffic situations from the text. Our code and dataset are available at https://github.com/ChyaZhang/ChatTraffic. |[2311.16203v2](http://arxiv.org/abs/2311.16203v2)|**[link](https://github.com/ChyaZhang/ChatTraffic)**|
|**2023-11-14**|**Brain-Driven Representation Learning Based on Diffusion Model**|cs.CL, cs.AI|Interpreting EEG signals linked to spoken language presents a complex challenge, given the data's intricate temporal and spatial attributes, as well as the various noise factors. Denoising diffusion probabilistic models (DDPMs), which have recently gained prominence in diverse areas for their capabilities in representation learning, are explored in our research as a means to address this issue. Using DDPMs in conjunction with a conditional autoencoder, our new approach considerably outperforms traditional machine learning algorithms and established baseline models in accuracy. Our results highlight the potential of DDPMs as a sophisticated computational method for the analysis of speech-related EEG signals. This could lead to significant advances in brain-computer interfaces tailored for spoken communication. |[2311.07925v1](http://arxiv.org/abs/2311.07925v1)|null|
|**2023-11-01**|**CodeFusion: A Pre-trained Diffusion Model for Code Generation**|cs.SE, cs.AI, cs.CL, cs.PL|Imagine a developer who can only change their last line of code, how often would they have to start writing a function from scratch before it is correct? Auto-regressive models for code generation from natural language have a similar limitation: they do not easily allow reconsidering earlier tokens generated. We introduce CodeFusion, a pre-trained diffusion code generation model that addresses this limitation by iteratively denoising a complete program conditioned on the encoded natural language. We evaluate CodeFusion on the task of natural language to code generation for Bash, Python, and Microsoft Excel conditional formatting (CF) rules. Experiments show that CodeFusion (75M parameters) performs on par with state-of-the-art auto-regressive systems (350M-175B parameters) in top-1 accuracy and outperforms them in top-3 and top-5 accuracy due to its better balance in diversity versus quality. |[2310.17680v3](http://arxiv.org/abs/2310.17680v3)|null|
|**2023-10-26**|**DiffS2UT: A Semantic Preserving Diffusion Model for Textless Direct Speech-to-Speech Translation**|cs.CL|While Diffusion Generative Models have achieved great success on image generation tasks, how to efficiently and effectively incorporate them into speech generation especially translation tasks remains a non-trivial problem. Specifically, due to the low information density of speech data, the transformed discrete speech unit sequence is much longer than the corresponding text transcription, posing significant challenges to existing auto-regressive models. Furthermore, it is not optimal to brutally apply discrete diffusion on the speech unit sequence while disregarding the continuous space structure, which will degrade the generation performance significantly. In this paper, we propose a novel diffusion model by applying the diffusion forward process in the \textit{continuous} speech representation space, while employing the diffusion backward process in the \textit{discrete} speech unit space. In this way, we preserve the semantic structure of the continuous speech representation space in the diffusion process and integrate the continuous and discrete diffusion models. We conduct extensive experiments on the textless direct speech-to-speech translation task, where the proposed method achieves comparable results to the computationally intensive auto-regressive baselines (500 steps on average) with significantly fewer decoding steps (50 steps). |[2310.17570v1](http://arxiv.org/abs/2310.17570v1)|null|
|**2023-10-25**|**Discrete Diffusion Language Modeling by Estimating the Ratios of the Data Distribution**|stat.ML, cs.CL, cs.LG|Despite their groundbreaking performance for many generative modeling tasks, diffusion models have fallen short on discrete data domains such as natural language. Crucially, standard diffusion models rely on the well-established theory of score matching, but efforts to generalize this to discrete structures have not yielded the same empirical gains. In this work, we bridge this gap by proposing score entropy, a novel discrete score matching loss that is more stable than existing methods, forms an ELBO for maximum likelihood training, and can be efficiently optimized with a denoising variant. We scale our Score Entropy Discrete Diffusion models (SEDD) to the experimental setting of GPT-2, achieving highly competitive likelihoods while also introducing distinct algorithmic advantages. In particular, when comparing similarly sized SEDD and GPT-2 models, SEDD attains comparable perplexities (normally within $+10\%$ of and sometimes outperforming the baseline). Furthermore, SEDD models learn a more faithful sequence distribution (around $4\times$ better compared to GPT-2 models with ancestral sampling as measured by large models), can trade off compute for generation quality (needing only $16\times$ fewer network evaluations to match GPT-2), and enables arbitrary infilling beyond the standard left to right prompting. |[2310.16834v1](http://arxiv.org/abs/2310.16834v1)|null|
|**2023-10-24**|**A Diffusion Weighted Graph Framework for New Intent Discovery**|cs.CL, cs.AI, cs.LG|New Intent Discovery (NID) aims to recognize both new and known intents from unlabeled data with the aid of limited labeled data containing only known intents. Without considering structure relationships between samples, previous methods generate noisy supervisory signals which cannot strike a balance between quantity and quality, hindering the formation of new intent clusters and effective transfer of the pre-training knowledge. To mitigate this limitation, we propose a novel Diffusion Weighted Graph Framework (DWGF) to capture both semantic similarities and structure relationships inherent in data, enabling more sufficient and reliable supervisory signals. Specifically, for each sample, we diffuse neighborhood relationships along semantic paths guided by the nearest neighbors for multiple hops to characterize its local structure discriminately. Then, we sample its positive keys and weigh them based on semantic similarities and local structures for contrastive learning. During inference, we further propose Graph Smoothing Filter (GSF) to explicitly utilize the structure relationships to filter high-frequency noise embodied in semantically ambiguous samples on the cluster boundary. Extensive experiments show that our method outperforms state-of-the-art models on all evaluation metrics across multiple benchmark datasets. Code and data are available at https://github.com/yibai-shi/DWGF. |[2310.15836v1](http://arxiv.org/abs/2310.15836v1)|**[link](https://github.com/yibai-shi/dwgf)**|
|**2023-10-24**|**ScanDL: A Diffusion Model for Generating Synthetic Scanpaths on Texts**|cs.CL|Eye movements in reading play a crucial role in psycholinguistic research studying the cognitive mechanisms underlying human language processing. More recently, the tight coupling between eye movements and cognition has also been leveraged for language-related machine learning tasks such as the interpretability, enhancement, and pre-training of language models, as well as the inference of reader- and text-specific properties. However, scarcity of eye movement data and its unavailability at application time poses a major challenge for this line of research. Initially, this problem was tackled by resorting to cognitive models for synthesizing eye movement data. However, for the sole purpose of generating human-like scanpaths, purely data-driven machine-learning-based methods have proven to be more suitable. Following recent advances in adapting diffusion processes to discrete data, we propose ScanDL, a novel discrete sequence-to-sequence diffusion model that generates synthetic scanpaths on texts. By leveraging pre-trained word representations and jointly embedding both the stimulus text and the fixation sequence, our model captures multi-modal interactions between the two inputs. We evaluate ScanDL within- and across-dataset and demonstrate that it significantly outperforms state-of-the-art scanpath generation methods. Finally, we provide an extensive psycholinguistic analysis that underlines the model's ability to exhibit human-like reading behavior. Our implementation is made available at https://github.com/DiLi-Lab/ScanDL. |[2310.15587v1](http://arxiv.org/abs/2310.15587v1)|**[link](https://github.com/dili-lab/scandl)**|
|**2023-10-23**|**DeTiME: Diffusion-Enhanced Topic Modeling using Encoder-decoder based LLM**|cs.CL, cs.AI, 68T50, I.2.7|In the burgeoning field of natural language processing, Neural Topic Models (NTMs) and Large Language Models (LLMs) have emerged as areas of significant research interest. Despite this, NTMs primarily utilize contextual embeddings from LLMs, which are not optimal for clustering or capable for topic generation. Our study addresses this gap by introducing a novel framework named Diffusion-Enhanced Topic Modeling using Encoder-Decoder-based LLMs (DeTiME). DeTiME leverages ncoder-Decoder-based LLMs to produce highly clusterable embeddings that could generate topics that exhibit both superior clusterability and enhanced semantic coherence compared to existing methods. Additionally, by exploiting the power of diffusion, our framework also provides the capability to generate content relevant to the identified topics. This dual functionality allows users to efficiently produce highly clustered topics and related content simultaneously. DeTiME's potential extends to generating clustered embeddings as well. Notably, our proposed framework proves to be efficient to train and exhibits high adaptability, demonstrating its potential for a wide array of applications. |[2310.15296v1](http://arxiv.org/abs/2310.15296v1)|null|
|**2023-10-18**|**InfoDiffusion: Information Entropy Aware Diffusion Process for Non-Autoregressive Text Generation**|cs.CL, cs.AI|Diffusion models have garnered considerable interest in the field of text generation. Several studies have explored text diffusion models with different structures and applied them to various tasks, including named entity recognition and summarization. However, there exists a notable disparity between the "easy-first" text generation process of current diffusion models and the "keyword-first" natural text generation process of humans, which has received limited attention. To bridge this gap, we propose InfoDiffusion, a non-autoregressive text diffusion model. Our approach introduces a "keyinfo-first" generation strategy and incorporates a noise schedule based on the amount of text information. In addition, InfoDiffusion combines self-conditioning with a newly proposed partially noising model structure. Experimental results show that InfoDiffusion outperforms the baseline model in terms of generation quality and diversity, as well as exhibiting higher sampling efficiency. |[2310.11976v1](http://arxiv.org/abs/2310.11976v1)|**[link](https://github.com/rzhwang/infodiffusion)**|
|**2023-10-16**|**ForceGen: End-to-end de novo protein generation based on nonlinear mechanical unfolding responses using a protein language diffusion model**|cond-mat.mtrl-sci, cond-mat.mes-hall, cs.CL, cs.LG, q-bio.BM|Through evolution, nature has presented a set of remarkable protein materials, including elastins, silks, keratins and collagens with superior mechanical performances that play crucial roles in mechanobiology. However, going beyond natural designs to discover proteins that meet specified mechanical properties remains challenging. Here we report a generative model that predicts protein designs to meet complex nonlinear mechanical property-design objectives. Our model leverages deep knowledge on protein sequences from a pre-trained protein language model and maps mechanical unfolding responses to create novel proteins. Via full-atom molecular simulations for direct validation, we demonstrate that the designed proteins are novel, and fulfill the targeted mechanical properties, including unfolding energy and mechanical strength, as well as the detailed unfolding force-separation curves. Our model offers rapid pathways to explore the enormous mechanobiological protein sequence space unconstrained by biological synthesis, using mechanical features as target to enable the discovery of protein materials with superior mechanical properties. |[2310.10605v1](http://arxiv.org/abs/2310.10605v1)|null|
|**2023-10-16**|**DiffuSeq-v2: Bridging Discrete and Continuous Text Spaces for Accelerated Seq2Seq Diffusion Models**|cs.LG, cs.CL|Diffusion models have gained prominence in generating high-quality sequences of text. Nevertheless, current approaches predominantly represent discrete text within a continuous diffusion space, which incurs substantial computational overhead during training and results in slower sampling speeds. In this paper, we introduce a soft absorbing state that facilitates the diffusion model in learning to reconstruct discrete mutations based on the underlying Gaussian space, thereby enhancing its capacity to recover conditional signals. During the sampling phase, we employ state-of-the-art ODE solvers within the continuous space to expedite the sampling process. Comprehensive experimental evaluations reveal that our proposed method effectively accelerates the training convergence by 4x and generates samples of similar quality 800x faster, rendering it significantly closer to practical application. \footnote{The code is released at \url{https://github.com/Shark-NLP/DiffuSeq} |[2310.05793v2](http://arxiv.org/abs/2310.05793v2)|**[link](https://github.com/Shark-NLP/DiffuSeq)**|
|**2023-09-25**|**Multiple Noises in Diffusion Model for Semi-Supervised Multi-Domain Translation**|cs.CL, cs.AI, cs.LG|Domain-to-domain translation involves generating a target domain sample given a condition in the source domain. Most existing methods focus on fixed input and output domains, i.e. they only work for specific configurations (i.e. for two domains, either $D_1\rightarrow{}D_2$ or $D_2\rightarrow{}D_1$). This paper proposes Multi-Domain Diffusion (MDD), a conditional diffusion framework for multi-domain translation in a semi-supervised context. Unlike previous methods, MDD does not require defining input and output domains, allowing translation between any partition of domains within a set (such as $(D_1, D_2)\rightarrow{}D_3$, $D_2\rightarrow{}(D_1, D_3)$, $D_3\rightarrow{}D_1$, etc. for 3 domains), without the need to train separate models for each domain configuration. The key idea behind MDD is to leverage the noise formulation of diffusion models by incorporating one noise level per domain, which allows missing domains to be modeled with noise in a natural way. This transforms the training task from a simple reconstruction task to a domain translation task, where the model relies on less noisy domains to reconstruct more noisy domains. We present results on a multi-domain (with more than two domains) synthetic image translation dataset with challenging semantic domain inversion. |[2309.14394v1](http://arxiv.org/abs/2309.14394v1)|null|
|**2023-09-04**|**ParaGuide: Guided Diffusion Paraphrasers for Plug-and-Play Textual Style Transfer**|cs.CL, cs.AI|Textual style transfer is the task of transforming stylistic properties of text while preserving meaning. Target "styles" can be defined in numerous ways, ranging from single attributes (e.g, formality) to authorship (e.g, Shakespeare). Previous unsupervised style-transfer approaches generally rely on significant amounts of labeled data for only a fixed set of styles or require large language models. In contrast, we introduce a novel diffusion-based framework for general-purpose style transfer that can be flexibly adapted to arbitrary target styles at inference time. Our parameter-efficient approach, ParaGuide, leverages paraphrase-conditioned diffusion models alongside gradient-based guidance from both off-the-shelf classifiers and strong existing style embedders to transform the style of text while preserving semantic information. We validate the method on the Enron Email Corpus, with both human and automatic evaluations, and find that it outperforms strong baselines on formality, sentiment, and even authorship style transfer. |[2308.15459v2](http://arxiv.org/abs/2308.15459v2)|**[link](https://github.com/zacharyhorvitz/ParaGuide)**|
|**2023-08-25**|**Diffusion Language Models Can Perform Many Tasks with Scaling and Instruction-Finetuning**|cs.CL, cs.AI, cs.LG|The recent surge of generative AI has been fueled by the generative power of diffusion probabilistic models and the scalable capabilities of large language models. Despite their potential, it remains elusive whether diffusion language models can solve general language tasks comparable to their autoregressive counterparts. This paper demonstrates that scaling diffusion models w.r.t. data, sizes, and tasks can effectively make them strong language learners. We build competent diffusion language models at scale by first acquiring knowledge from massive data via masked language modeling pretraining thanks to their intrinsic connections. We then reprogram pretrained masked language models into diffusion language models via diffusive adaptation, wherein task-specific finetuning and instruction finetuning are explored to unlock their versatility in solving general language tasks. Experiments show that scaling diffusion language models consistently improves performance across downstream language tasks. We further discover that instruction finetuning can elicit zero-shot and few-shot in-context learning abilities that help tackle many unseen tasks by following natural language instructions, and show promise in advanced and challenging abilities such as reasoning. |[2308.12219v2](http://arxiv.org/abs/2308.12219v2)|**[link](https://github.com/yegcjs/diffusionllm)**|
|**2023-08-17**|**Enhancing Phrase Representation by Information Bottleneck Guided Text Diffusion Process for Keyphrase Extraction**|cs.CL|Keyphrase extraction (KPE) is an important task in Natural Language Processing for many scenarios, which aims to extract keyphrases that are present in a given document. Many existing supervised methods treat KPE as sequential labeling, span-level classification, or generative tasks. However, these methods lack the ability to utilize keyphrase information, which may result in biased results. In this study, we propose Diff-KPE, which leverages the supervised Variational Information Bottleneck (VIB) to guide the text diffusion process for generating enhanced keyphrase representations. Diff-KPE first generates the desired keyphrase embeddings conditioned on the entire document and then injects the generated keyphrase embeddings into each phrase representation. A ranking network and VIB are then optimized together with rank loss and classification loss, respectively. This design of Diff-KPE allows us to rank each candidate phrase by utilizing both the information of keyphrases and the document. Experiments show that Diff-KPE outperforms existing KPE methods on a large open domain keyphrase extraction benchmark, OpenKP, and a scientific domain dataset, KP20K. |[2308.08739v1](http://arxiv.org/abs/2308.08739v1)|null|
|**2023-07-26**|**Founding a mathematical diffusion model in linguistics. The case study of German syntactic features in the North-Eastern Italian dialects**|cs.CL|We take as a case study the spread of Germanic syntactic features into Romance dialects of North-Eastern Italy, which occurred after the immigration of German people in the Tyrol during the High Middle Ages.   An interactive map is produced using tools of what is called Geographic Data Science. A smooth two-dimensional surface $\mathcal{G}$ expresses locally which fraction of territory uses a given German language feature: it is obtained by interpolating a discrete function that says if at any surveyed locality that feature is used or not.\newline   This surface $\mathcal{G}$ is thought of as the value at the present time of a function describing a diffusion-convection phenomenon in two dimensions (here said \emph{tidal} mode), which is subjected in a very natural way to the same equation, suitably contextualized, used in physics for a number of phenomenological facts like the heat diffusion. It is shown that solutions of this equation, evaluated at the present time, fit well with the data as interpolated by $\mathcal{G}$, thus providing convincing pictures of diffusion-convection of the linguistic features of the case study, albeit simplifications and approximations.\newline   Very importantly, it is shown that Schmidt's 'waves' can be counted among the solutions of the diffusion equation: superimposing Schmidt 'waves' to a 'tidal flooding' can reproduce complexities of real linguistic diffusion events. |[2307.14291v1](http://arxiv.org/abs/2307.14291v1)|null|
|**2023-07-26**|**How Does Diffusion Influence Pretrained Language Models on Out-of-Distribution Data?**|cs.CL, cs.AI|Transformer-based pretrained language models (PLMs) have achieved great success in modern NLP. An important advantage of PLMs is good out-of-distribution (OOD) robustness. Recently, diffusion models have attracted a lot of work to apply diffusion to PLMs. It remains under-explored how diffusion influences PLMs on OOD data. The core of diffusion models is a forward diffusion process which gradually applies Gaussian noise to inputs, and a reverse denoising process which removes noise. The noised input reconstruction is a fundamental ability of diffusion models. We directly analyze OOD robustness by measuring the reconstruction loss, including testing the abilities to reconstruct OOD data, and to detect OOD samples. Experiments are conducted by analyzing different training parameters and data statistical features on eight datasets. It shows that finetuning PLMs with diffusion degrades the reconstruction ability on OOD data. The comparison also shows that diffusion models can effectively detect OOD samples, achieving state-of-the-art performance in most of the datasets with an absolute accuracy improvement up to 18%. These results indicate that diffusion reduces OOD robustness of PLMs. |[2307.13949v1](http://arxiv.org/abs/2307.13949v1)|**[link](https://github.com/maybelizzy/diffusion_ood_robustness)**|
|**2023-07-31**|**XDLM: Cross-lingual Diffusion Language Model for Machine Translation**|cs.CL|Recently, diffusion models have excelled in image generation tasks and have also been applied to neural language processing (NLP) for controllable text generation. However, the application of diffusion models in a cross-lingual setting is less unexplored. Additionally, while pretraining with diffusion models has been studied within a single language, the potential of cross-lingual pretraining remains understudied. To address these gaps, we propose XDLM, a novel Cross-lingual diffusion model for machine translation, consisting of pretraining and fine-tuning stages. In the pretraining stage, we propose TLDM, a new training objective for mastering the mapping between different languages; in the fine-tuning stage, we build up the translation system based on the pretrained model. We evaluate the result on several machine translation benchmarks and outperformed both diffusion and Transformer baselines. |[2307.13560v2](http://arxiv.org/abs/2307.13560v2)|null|
|**2023-06-14**|**DiffuDetox: A Mixed Diffusion Model for Text Detoxification**|cs.CL, cs.LG|Text detoxification is a conditional text generation task aiming to remove offensive content from toxic text. It is highly useful for online forums and social media, where offensive content is frequently encountered. Intuitively, there are diverse ways to detoxify sentences while preserving their meanings, and we can select from detoxified sentences before displaying text to users. Conditional diffusion models are particularly suitable for this task given their demonstrated higher generative diversity than existing conditional text generation models based on language models. Nonetheless, text fluency declines when they are trained with insufficient data, which is the case for this task. In this work, we propose DiffuDetox, a mixed conditional and unconditional diffusion model for text detoxification. The conditional model takes toxic text as the condition and reduces its toxicity, yielding a diverse set of detoxified sentences. The unconditional model is trained to recover the input text, which allows the introduction of additional fluent text for training and thus ensures text fluency. Extensive experimental results and in-depth analysis demonstrate the effectiveness of our proposed DiffuDetox. |[2306.08505v1](http://arxiv.org/abs/2306.08505v1)|null|
|**2023-06-05**|**PLANNER: Generating Diversified Paragraph via Latent Language Diffusion Model**|cs.CL|Autoregressive models for text sometimes generate repetitive and low-quality output because errors accumulate during the steps of generation. This issue is often attributed to exposure bias - the difference between how a model is trained, and how it is used during inference. Denoising diffusion models provide an alternative approach in which a model can revisit and revise its output. However, they can be computationally expensive and prior efforts on text have led to models that produce less fluent output compared to autoregressive models, especially for longer text and paragraphs. In this paper, we propose PLANNER, a model that combines latent semantic diffusion with autoregressive generation, to generate fluent text while exercising global control over paragraphs. The model achieves this by combining an autoregressive "decoding" module with a "planning" module that uses latent diffusion to generate semantic paragraph embeddings in a coarse-to-fine manner. The proposed method is evaluated on various conditional generation tasks, and results on semantic generation, text completion and summarization show its effectiveness in generating high-quality long-form text in an efficient manner. |[2306.02531v1](http://arxiv.org/abs/2306.02531v1)|null|
|**2023-06-02**|**DiffusEmp: A Diffusion Model-Based Framework with Multi-Grained Control for Empathetic Response Generation**|cs.CL, cs.AI|Empathy is a crucial factor in open-domain conversations, which naturally shows one's caring and understanding to others. Though several methods have been proposed to generate empathetic responses, existing works often lead to monotonous empathy that refers to generic and safe expressions. In this paper, we propose to use explicit control to guide the empathy expression and design a framework DiffusEmp based on conditional diffusion language model to unify the utilization of dialogue context and attribute-oriented control signals. Specifically, communication mechanism, intent, and semantic frame are imported as multi-grained signals that control the empathy realization from coarse to fine levels. We then design a specific masking strategy to reflect the relationship between multi-grained signals and response tokens, and integrate it into the diffusion model to influence the generative process. Experimental results on a benchmark dataset EmpatheticDialogue show that our framework outperforms competitive baselines in terms of controllability, informativeness, and diversity without the loss of context-relatedness. |[2306.01657v1](http://arxiv.org/abs/2306.01657v1)|null|
|**2023-05-31**|**Fine-grained Text Style Transfer with Diffusion-Based Language Models**|cs.CL, cs.AI, cs.LG|Diffusion probabilistic models have shown great success in generating high-quality images controllably, and researchers have tried to utilize this controllability into text generation domain. Previous works on diffusion-based language models have shown that they can be trained without external knowledge (such as pre-trained weights) and still achieve stable performance and controllability. In this paper, we trained a diffusion-based model on StylePTB dataset, the standard benchmark for fine-grained text style transfers. The tasks in StylePTB requires much more refined control over the output text compared to tasks evaluated in previous works, and our model was able to achieve state-of-the-art performance on StylePTB on both individual and compositional transfers. Moreover, our model, trained on limited data from StylePTB without external knowledge, outperforms previous works that utilized pretrained weights, embeddings, and external grammar parsers, and this may indicate that diffusion-based language models have great potential under low-resource settings. |[2305.19512v1](http://arxiv.org/abs/2305.19512v1)|**[link](https://github.com/lvyiwei1/diffuseq_styleptb)**|
|**2023-05-30**|**Likelihood-Based Diffusion Language Models**|cs.CL, cs.LG|Despite a growing interest in diffusion-based language models, existing work has not shown that these models can attain nontrivial likelihoods on standard language modeling benchmarks. In this work, we take the first steps towards closing the likelihood gap between autoregressive and diffusion-based language models, with the goal of building and releasing a diffusion model which outperforms a small but widely-known autoregressive model. We pursue this goal through algorithmic improvements, scaling laws, and increased compute. On the algorithmic front, we introduce several methodological improvements for the maximum-likelihood training of diffusion language models. We then study scaling laws for our diffusion models and find compute-optimal training regimes which differ substantially from autoregressive models. Using our methods and scaling analysis, we train and release Plaid 1B, a large diffusion language model which outperforms GPT-2 124M in likelihood on benchmark datasets and generates fluent samples in unconditional and zero-shot control settings. |[2305.18619v1](http://arxiv.org/abs/2305.18619v1)|**[link](https://github.com/igul222/plaid)**|

<p align=right>(<a href=#Updated-on-20231209>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[contributors-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[forks-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/network/members
[stars-shield]: https://img.shields.io/github/stars/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[stars-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/stargazers
[issues-shield]: https://img.shields.io/github/issues/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[issues-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/issues

