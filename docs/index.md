---
layout: default
---

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.06.03

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#diffusion>diffusion</a></li>
  </ol>
</details>

## diffusion

| Date | Title | label | Abstract | PDF | Code |
|:---------|:---------------|:-------|:------------------|:------|:------|
|**2023-05-31**|**Fine-grained Text Style Transfer with Diffusion-Based Language Models**|cs.CL, cs.AI, cs.LG|Diffusion probabilistic models have shown great success in generating high-quality images controllably, and researchers have tried to utilize this controllability into text generation domain. Previous works on diffusion-based language models have shown that they can be trained without external knowledge (such as pre-trained weights) and still achieve stable performance and controllability. In this paper, we trained a diffusion-based model on StylePTB dataset, the standard benchmark for fine-grained text style transfers. The tasks in StylePTB requires much more refined control over the output text compared to tasks evaluated in previous works, and our model was able to achieve state-of-the-art performance on StylePTB on both individual and compositional transfers. Moreover, our model, trained on limited data from StylePTB without external knowledge, outperforms previous works that utilized pretrained weights, embeddings, and external grammar parsers, and this may indicate that diffusion-based language models have great potential under low-resource settings. |[2305.19512v1](http://arxiv.org/abs/2305.19512v1)|**[link](https://github.com/lvyiwei1/diffuseq_styleptb)**|
|**2023-05-30**|**Likelihood-Based Diffusion Language Models**|cs.CL, cs.LG|Despite a growing interest in diffusion-based language models, existing work has not shown that these models can attain nontrivial likelihoods on standard language modeling benchmarks. In this work, we take the first steps towards closing the likelihood gap between autoregressive and diffusion-based language models, with the goal of building and releasing a diffusion model which outperforms a small but widely-known autoregressive model. We pursue this goal through algorithmic improvements, scaling laws, and increased compute. On the algorithmic front, we introduce several methodological improvements for the maximum-likelihood training of diffusion language models. We then study scaling laws for our diffusion models and find compute-optimal training regimes which differ substantially from autoregressive models. Using our methods and scaling analysis, we train and release Plaid 1B, a large diffusion language model which outperforms GPT-2 124M in likelihood on benchmark datasets and generates fluent samples in unconditional and zero-shot control settings. |[2305.18619v1](http://arxiv.org/abs/2305.18619v1)|**[link](https://github.com/igul222/plaid)**|
|**2023-05-27**|**A Diffusion Model for Event Skeleton Generation**|cs.CL|Event skeleton generation, aiming to induce an event schema skeleton graph with abstracted event nodes and their temporal relations from a set of event instance graphs, is a critical step in the temporal complex event schema induction task. Existing methods effectively address this task from a graph generation perspective but suffer from noise-sensitive and error accumulation, e.g., the inability to correct errors while generating schema. We, therefore, propose a novel Diffusion Event Graph Model~(DEGM) to address these issues. Our DEGM is the first workable diffusion model for event skeleton generation, where the embedding and rounding techniques with a custom edge-based loss are introduced to transform a discrete event graph into learnable latent representation. Furthermore, we propose a denoising training process to maintain the model's robustness. Consequently, DEGM derives the final schema, where error correction is guaranteed by iteratively refining the latent representation during the schema generation process. Experimental results on three IED bombing datasets demonstrate that our DEGM achieves better results than other state-of-the-art baselines. Our code and data are available at https://github.com/zhufq00/EventSkeletonGeneration. |[2305.17458v1](http://arxiv.org/abs/2305.17458v1)|null|

<p align=right>(<a href=#Updated-on-20230603>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[contributors-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[forks-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/network/members
[stars-shield]: https://img.shields.io/github/stars/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[stars-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/stargazers
[issues-shield]: https://img.shields.io/github/issues/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[issues-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/issues

