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
    <li><a href=#text-generation>text generation</a></li>
  </ol>
</details>

## diffusion

| Publish Date | Title |Categories| Abstract | PDF | Code |
|:---------|:------------------|:------|:-----------------|:------|:------|
|**2023-06-01**|**Diffuse Sources, Clustering and the Excess Anisotropy of the Radio Synchrotron Background**|['astro-ph.CO', 'astro-ph.IM']|We present the largest low frequency (120~MHz) arcminute resolution image of the radio synchrotron background (RSB) to date, and its corresponding angular power spectrum of anisotropies (APS) with angular scales ranging from $3^\circ$ to $0.3^\prime$. We show that the RSB around the North Celestial Pole has a significant excess anisotropy power at all scales over a model of unclustered point sources based on source counts of known source classes. This anisotropy excess, which does not seem attributable to the diffuse Galactic emission, could be linked to the surface brightness excess of the RSB. To better understand the information contained within the measured APS, we model the RSB varying the brightness distribution, size, and angular clustering of potential sources. We show that the observed APS could be produced by a population of faint clustered point sources only if the clustering is extreme and the size of the Gaussian clusters is $\lesssim 1'$. We also show that the observed APS could be produced by a population of faint diffuse sources with sizes $\lesssim 1'$, and this is supported by features present in our image. Both of these cases would also cause an associated surface brightness excess. These classes of sources are in a parameter space not well probed by even the deepest radio surveys to date. |[2306.00829v1](http://arxiv.org/abs/2306.00829v1)|null|

<p align=right>(<a href=#Updated-on-20230603>back to top</a>)</p>

## text generation

| Publish Date | Title |Categories| Abstract | PDF | Code |
|:---------|:------------------|:------|:-----------------|:------|:------|
|**2023-06-01**|**Finite Entanglement Entropy in String Theory**|['hep-th', 'gr-qc', 'math-ph', 'math.MP', 'quant-ph']|We analyze the one-loop quantum entanglement entropy in ten-dimensional Type-II string theory using the orbifold method by analytically continuing in $N$ the genus-one partition function for string orbifolds on $\mathbb{R}^2/\mathbb{Z}_N$ conical spaces known for all odd integers $N > 1$. We show that the tachyonic contributions to the orbifold partition function can be appropriately summed and analytically continued to an expression that is finite in the physical region $0 < N \leq 1$ resulting in a finite and calculable answer for the entanglement entropy. We discuss the implications of the finiteness of the entanglement entropy for the information paradox, quantum gravity, and holography. |[2306.00990v1](http://arxiv.org/abs/2306.00990v1)|null|
|**2023-06-01**|**AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration**|['cs.CL']|Large language models (LLMs) have shown excellent performance on various tasks, but the astronomical model size raises the hardware barrier for serving (memory size) and slows down token generation (memory bandwidth). In this paper, we propose Activation-aware Weight Quantization (AWQ), a hardware-friendly approach for LLM low-bit weight-only quantization. Our method is based on the observation that weights are not equally important: protecting only 1% of salient weights can greatly reduce quantization error. We then propose to search for the optimal per-channel scaling that protects the salient weights by observing the activation, not weights. AWQ does not rely on any backpropagation or reconstruction, so it can well preserve LLMs' generalization ability on different domains and modalities, without overfitting to the calibration set; it also does not rely on any data layout reordering, maintaining the hardware efficiency. AWQ outperforms existing work on various language modeling, common sense QA, and domain-specific benchmarks. Thanks to better generalization, it achieves excellent quantization performance for instruction-tuned LMs and, for the first time, multi-modal LMs. We also implement efficient tensor core kernels with reorder-free online dequantization to accelerate AWQ, achieving a 1.45x speedup over GPTQ and is 1.85x faster than the cuBLAS FP16 implementation. Our method provides a turn-key solution to compress LLMs to 3/4 bits for efficient deployment. |[2306.00978v1](http://arxiv.org/abs/2306.00978v1)|**[link](https://github.com/mit-han-lab/llm-awq)**|

<p align=right>(<a href=#Updated-on-20230603>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[contributors-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[forks-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/network/members
[stars-shield]: https://img.shields.io/github/stars/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[stars-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/stargazers
[issues-shield]: https://img.shields.io/github/issues/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[issues-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/issues

