[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.06.06

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#diffusion>diffusion</a></li>
    <li><a href=#topic-model>topic model</a></li>
  </ol>
</details>

## diffusion

|Date|Title|label|Abstract|PDF|Code|
|---|---|---|---|---|---|
|**2023-06-05**|**PLANNER: Generating Diversified Paragraph via Latent Language Diffusion Model**|cs.CL|Autoregressive models for text sometimes generate repetitive and low-quality output because errors accumulate during the steps of generation. This issue is often attributed to exposure bias - the difference between how a model is trained, and how it is used during inference. Denoising diffusion models provide an alternative approach in which a model can revisit and revise its output. However, they can be computationally expensive and prior efforts on text have led to models that produce less fluent output compared to autoregressive models, especially for longer text and paragraphs. In this paper, we propose PLANNER, a model that combines latent semantic diffusion with autoregressive generation, to generate fluent text while exercising global control over paragraphs. The model achieves this by combining an autoregressive "decoding" module with a "planning" module that uses latent diffusion to generate semantic paragraph embeddings in a coarse-to-fine manner. The proposed method is evaluated on various conditional generation tasks, and results on semantic generation, text completion and summarization show its effectiveness in generating high-quality long-form text in an efficient manner. |[2306.02531v1](http://arxiv.org/abs/2306.02531v1)|null|
|**2023-06-02**|**DiffusEmp: A Diffusion Model-Based Framework with Multi-Grained Control for Empathetic Response Generation**|cs.CL, cs.AI|Empathy is a crucial factor in open-domain conversations, which naturally shows one's caring and understanding to others. Though several methods have been proposed to generate empathetic responses, existing works often lead to monotonous empathy that refers to generic and safe expressions. In this paper, we propose to use explicit control to guide the empathy expression and design a framework DiffusEmp based on conditional diffusion language model to unify the utilization of dialogue context and attribute-oriented control signals. Specifically, communication mechanism, intent, and semantic frame are imported as multi-grained signals that control the empathy realization from coarse to fine levels. We then design a specific masking strategy to reflect the relationship between multi-grained signals and response tokens, and integrate it into the diffusion model to influence the generative process. Experimental results on a benchmark dataset EmpatheticDialogue show that our framework outperforms competitive baselines in terms of controllability, informativeness, and diversity without the loss of context-relatedness. |[2306.01657v1](http://arxiv.org/abs/2306.01657v1)|null|
|**2023-05-31**|**Fine-grained Text Style Transfer with Diffusion-Based Language Models**|cs.CL, cs.AI, cs.LG|Diffusion probabilistic models have shown great success in generating high-quality images controllably, and researchers have tried to utilize this controllability into text generation domain. Previous works on diffusion-based language models have shown that they can be trained without external knowledge (such as pre-trained weights) and still achieve stable performance and controllability. In this paper, we trained a diffusion-based model on StylePTB dataset, the standard benchmark for fine-grained text style transfers. The tasks in StylePTB requires much more refined control over the output text compared to tasks evaluated in previous works, and our model was able to achieve state-of-the-art performance on StylePTB on both individual and compositional transfers. Moreover, our model, trained on limited data from StylePTB without external knowledge, outperforms previous works that utilized pretrained weights, embeddings, and external grammar parsers, and this may indicate that diffusion-based language models have great potential under low-resource settings. |[2305.19512v1](http://arxiv.org/abs/2305.19512v1)|**[link](https://github.com/lvyiwei1/diffuseq_styleptb)**|
|**2023-05-30**|**Likelihood-Based Diffusion Language Models**|cs.CL, cs.LG|Despite a growing interest in diffusion-based language models, existing work has not shown that these models can attain nontrivial likelihoods on standard language modeling benchmarks. In this work, we take the first steps towards closing the likelihood gap between autoregressive and diffusion-based language models, with the goal of building and releasing a diffusion model which outperforms a small but widely-known autoregressive model. We pursue this goal through algorithmic improvements, scaling laws, and increased compute. On the algorithmic front, we introduce several methodological improvements for the maximum-likelihood training of diffusion language models. We then study scaling laws for our diffusion models and find compute-optimal training regimes which differ substantially from autoregressive models. Using our methods and scaling analysis, we train and release Plaid 1B, a large diffusion language model which outperforms GPT-2 124M in likelihood on benchmark datasets and generates fluent samples in unconditional and zero-shot control settings. |[2305.18619v1](http://arxiv.org/abs/2305.18619v1)|**[link](https://github.com/igul222/plaid)**|
|**2023-05-27**|**A Diffusion Model for Event Skeleton Generation**|cs.CL|Event skeleton generation, aiming to induce an event schema skeleton graph with abstracted event nodes and their temporal relations from a set of event instance graphs, is a critical step in the temporal complex event schema induction task. Existing methods effectively address this task from a graph generation perspective but suffer from noise-sensitive and error accumulation, e.g., the inability to correct errors while generating schema. We, therefore, propose a novel Diffusion Event Graph Model~(DEGM) to address these issues. Our DEGM is the first workable diffusion model for event skeleton generation, where the embedding and rounding techniques with a custom edge-based loss are introduced to transform a discrete event graph into learnable latent representation. Furthermore, we propose a denoising training process to maintain the model's robustness. Consequently, DEGM derives the final schema, where error correction is guaranteed by iteratively refining the latent representation during the schema generation process. Experimental results on three IED bombing datasets demonstrate that our DEGM achieves better results than other state-of-the-art baselines. Our code and data are available at https://github.com/zhufq00/EventSkeletonGeneration. |[2305.17458v1](http://arxiv.org/abs/2305.17458v1)|null|

<p align=right>(<a href=#Updated-on-20230606>back to top</a>)</p>

## topic model

|Date|Title|label|Abstract|PDF|Code|
|---|---|---|---|---|---|
|**2023-06-02**|**Improving Generalization in Task-oriented Dialogues with Workflows and Action Plans**|cs.CL, cs.AI|Task-oriented dialogue is difficult in part because it involves understanding user intent, collecting information from the user, executing API calls, and generating helpful and fluent responses. However, for complex tasks one must also correctly do all of these things over multiple steps, and in a specific order. While large pre-trained language models can be fine-tuned end-to-end to create multi-step task-oriented dialogue agents that generate fluent text, our experiments confirm that this approach alone cannot reliably perform new multi-step tasks that are unseen during training. To address these limitations, we augment the dialogue contexts given to \textmd{text2text} transformers with known \textit{valid workflow names} and \textit{action plans}. Action plans consist of sequences of actions required to accomplish a task, and are encoded as simple sequences of keywords (e.g. verify-identity, pull-up-account, reset-password, etc.). We perform extensive experiments on the Action-Based Conversations Dataset (ABCD) with T5-small, base and large models, and show that such models: a) are able to more readily generalize to unseen workflows by following the provided plan, and b) are able to generalize to executing unseen actions if they are provided in the plan. In contrast, models are unable to fully accomplish new multi-step tasks when they are not provided action plan information, even when given new valid workflow names. |[2306.01729v1](http://arxiv.org/abs/2306.01729v1)|null|
|**2023-06-02**|**Distilling Efficient Language-Specific Models for Cross-Lingual Transfer**|cs.CL|Massively multilingual Transformers (MMTs), such as mBERT and XLM-R, are widely used for cross-lingual transfer learning. While these are pretrained to represent hundreds of languages, end users of NLP systems are often interested only in individual languages. For such purposes, the MMTs' language coverage makes them unnecessarily expensive to deploy in terms of model size, inference time, energy, and hardware cost. We thus propose to extract compressed, language-specific models from MMTs which retain the capacity of the original MMTs for cross-lingual transfer. This is achieved by distilling the MMT bilingually, i.e., using data from only the source and target language of interest. Specifically, we use a two-phase distillation approach, termed BiStil: (i) the first phase distils a general bilingual model from the MMT, while (ii) the second, task-specific phase sparsely fine-tunes the bilingual "student" model using a task-tuned variant of the original MMT as its "teacher". We evaluate this distillation technique in zero-shot cross-lingual transfer across a number of standard cross-lingual benchmarks. The key results indicate that the distilled models exhibit minimal degradation in target language performance relative to the base MMT despite being significantly smaller and faster. Furthermore, we find that they outperform multilingually distilled models such as DistilmBERT and MiniLMv2 while having a very modest training budget in comparison, even on a per-language basis. We also show that bilingual models distilled from MMTs greatly outperform bilingual models trained from scratch. Our code and models are available at https://github.com/AlanAnsell/bistil. |[2306.01709v1](http://arxiv.org/abs/2306.01709v1)|**[link](https://github.com/alanansell/bistil)**|
|**2023-06-02**|**Learning Multi-step Reasoning from Arithmetic Task**|cs.CL|Mathematical reasoning is regarded as a necessary ability for Language Models (LMs). Recent works demonstrate large LMs' impressive performance in solving math problems. The success is attributed to their Chain-of-Thought (CoT) reasoning abilities, i.e., the ability to decompose complex questions into step-by-step reasoning chains, but such ability seems only to emerge from models with abundant parameters. This work investigates how to incorporate relatively small LMs with the capabilities of multi-step reasoning. We propose to inject such abilities by continually pre-training LMs on a synthetic dataset MsAT, which stands for Multi-step Arithmetic Task. Our experiments on four math word problem datasets show the effectiveness of the proposed method in enhancing LMs' math reasoning abilities. |[2306.01707v1](http://arxiv.org/abs/2306.01707v1)|**[link](https://github.com/TianduoWang/MsAT)**|
|**2023-06-02**|**Fine-Grained Human Feedback Gives Better Rewards for Language Model Training**|cs.CL|Language models (LMs) often exhibit undesirable text generation behaviors, including generating false, toxic, or irrelevant outputs. Reinforcement learning from human feedback (RLHF) - where human preference judgments on LM outputs are transformed into a learning signal - has recently shown promise in addressing these issues. However, such holistic feedback conveys limited information on long text outputs; it does not indicate which aspects of the outputs influenced user preference; e.g., which parts contain what type(s) of errors. In this paper, we use fine-grained human feedback (e.g., which sentence is false, which sub-sentence is irrelevant) as an explicit training signal. We introduce Fine-Grained RLHF, a framework that enables training and learning from reward functions that are fine-grained in two respects: (1) density, providing a reward after every segment (e.g., a sentence) is generated; and (2) incorporating multiple reward models associated with different feedback types (e.g., factual incorrectness, irrelevance, and information incompleteness). We conduct experiments on detoxification and long-form question answering to illustrate how learning with such reward functions leads to improved performance, supported by both automatic and human evaluation. Additionally, we show that LM behaviors can be customized using different combinations of fine-grained reward models. We release all data, collected human feedback, and codes at https://FineGrainedRLHF.github.io. |[2306.01693v1](http://arxiv.org/abs/2306.01693v1)|null|
|**2023-06-02**|**DiffusEmp: A Diffusion Model-Based Framework with Multi-Grained Control for Empathetic Response Generation**|cs.CL, cs.AI|Empathy is a crucial factor in open-domain conversations, which naturally shows one's caring and understanding to others. Though several methods have been proposed to generate empathetic responses, existing works often lead to monotonous empathy that refers to generic and safe expressions. In this paper, we propose to use explicit control to guide the empathy expression and design a framework DiffusEmp based on conditional diffusion language model to unify the utilization of dialogue context and attribute-oriented control signals. Specifically, communication mechanism, intent, and semantic frame are imported as multi-grained signals that control the empathy realization from coarse to fine levels. We then design a specific masking strategy to reflect the relationship between multi-grained signals and response tokens, and integrate it into the diffusion model to influence the generative process. Experimental results on a benchmark dataset EmpatheticDialogue show that our framework outperforms competitive baselines in terms of controllability, informativeness, and diversity without the loss of context-relatedness. |[2306.01657v1](http://arxiv.org/abs/2306.01657v1)|null|
|**2023-06-02**|**Learning from Partially Annotated Data: Example-aware Creation of Gap-filling Exercises for Language Learning**|cs.CL|Since performing exercises (including, e.g., practice tests) forms a crucial component of learning, and creating such exercises requires non-trivial effort from the teacher. There is a great value in automatic exercise generation in digital tools in education. In this paper, we particularly focus on automatic creation of gapfilling exercises for language learning, specifically grammar exercises. Since providing any annotation in this domain requires human expert effort, we aim to avoid it entirely and explore the task of converting existing texts into new gap-filling exercises, purely based on an example exercise, without explicit instruction or detailed annotation of the intended grammar topics. We contribute (i) a novel neural network architecture specifically designed for aforementioned gap-filling exercise generation task, and (ii) a real-world benchmark dataset for French grammar. We show that our model for this French grammar gap-filling exercise generation outperforms a competitive baseline classifier by 8% in F1 percentage points, achieving an average F1 score of 82%. Our model implementation and the dataset are made publicly available to foster future research, thus offering a standardized evaluation and baseline solution of the proposed partially annotated data prediction task in grammar exercise creation. |[2306.01584v1](http://arxiv.org/abs/2306.01584v1)|**[link](https://github.com/semerekiros/gf2)**|
|**2023-06-02**|**EmoUS: Simulating User Emotions in Task-Oriented Dialogues**|cs.CL|Existing user simulators (USs) for task-oriented dialogue systems only model user behaviour on semantic and natural language levels without considering the user persona and emotions. Optimising dialogue systems with generic user policies, which cannot model diverse user behaviour driven by different emotional states, may result in a high drop-off rate when deployed in the real world. Thus, we present EmoUS, a user simulator that learns to simulate user emotions alongside user behaviour. EmoUS generates user emotions, semantic actions, and natural language responses based on the user goal, the dialogue history, and the user persona. By analysing what kind of system behaviour elicits what kind of user emotions, we show that EmoUS can be used as a probe to evaluate a variety of dialogue systems and in particular their effect on the user's emotional state. Developing such methods is important in the age of large language model chat-bots and rising ethical concerns. |[2306.01579v1](http://arxiv.org/abs/2306.01579v1)|null|
|**2023-06-02**|**Comparing a composite model versus chained models to locate a nearest visual object**|cs.CL|Extracting information from geographic images and text is crucial for autonomous vehicles to determine in advance the best cell stations to connect to along their future path. Multiple artificial neural network models can address this challenge; however, there is no definitive guidance on the selection of an appropriate model for such use cases. Therefore, we experimented two architectures to solve such a task: a first architecture with chained models where each model in the chain addresses a sub-task of the task; and a second architecture with a single model that addresses the whole task. Our results showed that these two architectures achieved the same level performance with a root mean square error (RMSE) of 0.055 and 0.056; The findings further revealed that when the task can be decomposed into sub-tasks, the chain architecture exhibits a twelve-fold increase in training speed compared to the composite model. Nevertheless, the composite model significantly alleviates the burden of data labeling. |[2306.01551v1](http://arxiv.org/abs/2306.01551v1)|null|
|**2023-06-02**|**PassGPT: Password Modeling and (Guided) Generation with Large Language Models**|cs.CL, cs.AI, cs.CR|Large language models (LLMs) successfully model natural language from vast amounts of text without the need for explicit supervision. In this paper, we investigate the efficacy of LLMs in modeling passwords. We present PassGPT, a LLM trained on password leaks for password generation. PassGPT outperforms existing methods based on generative adversarial networks (GAN) by guessing twice as many previously unseen passwords. Furthermore, we introduce the concept of guided password generation, where we leverage PassGPT sampling procedure to generate passwords matching arbitrary constraints, a feat lacking in current GAN-based strategies. Lastly, we conduct an in-depth analysis of the entropy and probability distribution that PassGPT defines over passwords and discuss their use in enhancing existing password strength estimators. |[2306.01545v1](http://arxiv.org/abs/2306.01545v1)|null|
|**2023-06-01**|**AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration**|cs.CL|Large language models (LLMs) have shown excellent performance on various tasks, but the astronomical model size raises the hardware barrier for serving (memory size) and slows down token generation (memory bandwidth). In this paper, we propose Activation-aware Weight Quantization (AWQ), a hardware-friendly approach for LLM low-bit weight-only quantization. Our method is based on the observation that weights are not equally important: protecting only 1% of salient weights can greatly reduce quantization error. We then propose to search for the optimal per-channel scaling that protects the salient weights by observing the activation, not weights. AWQ does not rely on any backpropagation or reconstruction, so it can well preserve LLMs' generalization ability on different domains and modalities, without overfitting to the calibration set; it also does not rely on any data layout reordering, maintaining the hardware efficiency. AWQ outperforms existing work on various language modeling, common sense QA, and domain-specific benchmarks. Thanks to better generalization, it achieves excellent quantization performance for instruction-tuned LMs and, for the first time, multi-modal LMs. We also implement efficient tensor core kernels with reorder-free online dequantization to accelerate AWQ, achieving a 1.45x speedup over GPTQ and is 1.85x faster than the cuBLAS FP16 implementation. Our method provides a turn-key solution to compress LLMs to 3/4 bits for efficient deployment. |[2306.00978v1](http://arxiv.org/abs/2306.00978v1)|**[link](https://github.com/mit-han-lab/llm-awq)**|
|**2023-06-02**|**TopEx: Topic-based Explanations for Model Comparison**|cs.CL|Meaningfully comparing language models is challenging with current explanation methods. Current explanations are overwhelming for humans due to large vocabularies or incomparable across models. We present TopEx, an explanation method that enables a level playing field for comparing language models via model-agnostic topics. We demonstrate how TopEx can identify similarities and differences between DistilRoBERTa and GPT-2 on a variety of NLP tasks. |[2306.00976v2](http://arxiv.org/abs/2306.00976v2)|null|
|**2023-06-01**|**EEL: Efficiently Encoding Lattices for Reranking**|cs.CL, cs.AI, cs.LG|Standard decoding approaches for conditional text generation tasks typically search for an output hypothesis with high model probability, but this may not yield the best hypothesis according to human judgments of quality. Reranking to optimize for "downstream" metrics can better optimize for quality, but many metrics of interest are computed with pre-trained language models, which are slow to apply to large numbers of hypotheses. We explore an approach for reranking hypotheses by using Transformers to efficiently encode lattices of generated outputs, a method we call EEL. With a single Transformer pass over the entire lattice, we can approximately compute a contextualized representation of each token as if it were only part of a single hypothesis in isolation. We combine this approach with a new class of token-factored rerankers (TFRs) that allow for efficient extraction of high reranker-scoring hypotheses from the lattice. Empirically, our approach incurs minimal degradation error compared to the exponentially slower approach of encoding each hypothesis individually. When applying EEL with TFRs across three text generation tasks, our results show both substantial speedup compared to naive reranking and often better performance on downstream metrics than comparable approaches. |[2306.00947v1](http://arxiv.org/abs/2306.00947v1)|**[link](https://github.com/prasanns/eel-reranking)**|
|**2023-06-01**|**Exposing Attention Glitches with Flip-Flop Language Modeling**|cs.LG, cs.CL|Why do large language models sometimes output factual inaccuracies and exhibit erroneous reasoning? The brittleness of these models, particularly when executing long chains of reasoning, currently seems to be an inevitable price to pay for their advanced capabilities of coherently synthesizing knowledge, pragmatics, and abstract thought. Towards making sense of this fundamentally unsolved problem, this work identifies and analyzes the phenomenon of attention glitches, in which the Transformer architecture's inductive biases intermittently fail to capture robust reasoning. To isolate the issue, we introduce flip-flop language modeling (FFLM), a parametric family of synthetic benchmarks designed to probe the extrapolative behavior of neural language models. This simple generative task requires a model to copy binary symbols over long-range dependencies, ignoring the tokens in between. We find that Transformer FFLMs suffer from a long tail of sporadic reasoning errors, some of which we can eliminate using various regularization techniques. Our preliminary mechanistic analyses show why the remaining errors may be very difficult to diagnose and resolve. We hypothesize that attention glitches account for (some of) the closed-domain hallucinations in natural LLMs. |[2306.00946v1](http://arxiv.org/abs/2306.00946v1)|null|
|**2023-06-01**|**AMR4NLI: Interpretable and robust NLI measures from semantic graphs**|cs.CL, cs.IR|The task of natural language inference (NLI) asks whether a given premise (expressed in NL) entails a given NL hypothesis. NLI benchmarks contain human ratings of entailment, but the meaning relationships driving these ratings are not formalized. Can the underlying sentence pair relationships be made more explicit in an interpretable yet robust fashion? We compare semantic structures to represent premise and hypothesis, including sets of contextualized embeddings and semantic graphs (Abstract Meaning Representations), and measure whether the hypothesis is a semantic substructure of the premise, utilizing interpretable metrics. Our evaluation on three English benchmarks finds value in both contextualized embeddings and semantic graphs; moreover, they provide complementary signals, and can be leveraged together in a hybrid model. |[2306.00936v1](http://arxiv.org/abs/2306.00936v1)|null|
|**2023-06-01**|**ACLM: A Selective-Denoising based Generative Data Augmentation Approach for Low-Resource Complex NER**|cs.CL, cs.AI, cs.IR|Complex Named Entity Recognition (NER) is the task of detecting linguistically complex named entities in low-context text. In this paper, we present ACLM Attention-map aware keyword selection for Conditional Language Model fine-tuning), a novel data augmentation approach based on conditional generation to address the data scarcity problem in low-resource complex NER. ACLM alleviates the context-entity mismatch issue, a problem existing NER data augmentation techniques suffer from and often generates incoherent augmentations by placing complex named entities in the wrong context. ACLM builds on BART and is optimized on a novel text reconstruction or denoising task - we use selective masking (aided by attention maps) to retain the named entities and certain keywords in the input sentence that provide contextually relevant additional knowledge or hints about the named entities. Compared with other data augmentation strategies, ACLM can generate more diverse and coherent augmentations preserving the true word sense of complex entities in the sentence. We demonstrate the effectiveness of ACLM both qualitatively and quantitatively on monolingual, cross-lingual, and multilingual complex NER across various low-resource settings. ACLM outperforms all our neural baselines by a significant margin (1%-36%). In addition, we demonstrate the application of ACLM to other domains that suffer from data scarcity (e.g., biomedical). In practice, ACLM generates more effective and factual augmentations for these domains than prior methods. Code: https://github.com/Sreyan88/ACLM |[2306.00928v1](http://arxiv.org/abs/2306.00928v1)|**[link](https://github.com/sreyan88/aclm)**|
|**2023-06-01**|**Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker**|cs.CL, cs.AI, cs.LG|Theory of Mind (ToM)$\unicode{x2014}$the ability to reason about the mental states of other people$\unicode{x2014}$is a key element of our social intelligence. Yet, despite their ever more impressive performance, large-scale neural language models still lack basic theory of mind capabilities out-of-the-box. We posit that simply scaling up models will not imbue them with theory of mind due to the inherently symbolic and implicit nature of the phenomenon, and instead investigate an alternative: can we design a decoding-time algorithm that enhances theory of mind of off-the-shelf neural language models without explicit supervision? We present SymbolicToM, a plug-and-play approach to reason about the belief states of multiple characters in reading comprehension tasks via explicit symbolic representation. More concretely, our approach tracks each entity's beliefs, their estimation of other entities' beliefs, and higher-order levels of reasoning, all through graphical representations, allowing for more precise and interpretable reasoning than previous approaches. Empirical results on the well-known ToMi benchmark (Le et al., 2019) demonstrate that SymbolicToM dramatically enhances off-the-shelf neural networks' theory of mind in a zero-shot setting while showing robust out-of-distribution performance compared to supervised baselines. Our work also reveals spurious patterns in existing theory of mind benchmarks, emphasizing the importance of out-of-distribution evaluation and methods that do not overfit a particular dataset. |[2306.00924v1](http://arxiv.org/abs/2306.00924v1)|null|
|**2023-06-01**|**OpenPI-C: A Better Benchmark and Stronger Baseline for Open-Vocabulary State Tracking**|cs.CL|Open-vocabulary state tracking is a more practical version of state tracking that aims to track state changes of entities throughout a process without restricting the state space and entity space. OpenPI is to date the only dataset annotated for open-vocabulary state tracking. However, we identify issues with the dataset quality and evaluation metric. For the dataset, we categorize 3 types of problems on the procedure level, step level and state change level respectively, and build a clean dataset OpenPI-C using multiple rounds of human judgment. For the evaluation metric, we propose a cluster-based metric to fix the original metric's preference for repetition.   Model-wise, we enhance the seq2seq generation baseline by reinstating two key properties for state tracking: temporal dependency and entity awareness. The state of the world after an action is inherently dependent on the previous state. We model this dependency through a dynamic memory bank and allow the model to attend to the memory slots during decoding. On the other hand, the state of the world is naturally a union of the states of involved entities. Since the entities are unknown in the open-vocabulary setting, we propose a two-stage model that refines the state change prediction conditioned on entities predicted from the first stage. Empirical results show the effectiveness of our proposed model especially on the cluster-based metric. The code and data are released at https://github.com/shirley-wu/openpi-c |[2306.00887v1](http://arxiv.org/abs/2306.00887v1)|**[link](https://github.com/shirley-wu/openpi-c)**|
|**2023-06-01**|**Adversarial learning of neural user simulators for dialogue policy optimisation**|cs.CL|Reinforcement learning based dialogue policies are typically trained in interaction with a user simulator. To obtain an effective and robust policy, this simulator should generate user behaviour that is both realistic and varied. Current data-driven simulators are trained to accurately model the user behaviour in a dialogue corpus. We propose an alternative method using adversarial learning, with the aim to simulate realistic user behaviour with more variation. We train and evaluate several simulators on a corpus of restaurant search dialogues, and then use them to train dialogue system policies. In policy cross-evaluation experiments we demonstrate that an adversarially trained simulator produces policies with 8.3% higher success rate than those trained with a maximum likelihood simulator. Subjective results from a crowd-sourced dialogue system user evaluation confirm the effectiveness of adversarially training user simulators. |[2306.00858v1](http://arxiv.org/abs/2306.00858v1)|null|
|**2023-06-01**|**Zero and Few-shot Semantic Parsing with Ambiguous Inputs**|cs.CL|Despite the ubiquity of ambiguity in natural language, it is often ignored or deliberately removed in semantic parsing tasks, which generally assume that a given surface form has only one correct logical form. We attempt to address this shortcoming by introducing AmP, a framework, dataset, and challenge for parsing with linguistic ambiguity. We define templates and generate data for five well-documented linguistic ambiguities. Using AmP, we investigate how several few-shot semantic parsing systems handle ambiguity, introducing three new metrics. We find that large pre-trained models perform poorly at capturing the distribution of possible meanings without deliberate instruction. However, models are able to capture distribution well when ambiguity is attested in their inputs. These results motivate a call for ambiguity to be explicitly included in semantic parsing, and promotes considering the distribution of possible outputs when evaluating semantic parsing systems. |[2306.00824v1](http://arxiv.org/abs/2306.00824v1)|**[link](https://github.com/esteng/ambiguous_parsing)**|

<p align=right>(<a href=#Updated-on-20230606>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[contributors-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[forks-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/network/members
[stars-shield]: https://img.shields.io/github/stars/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[stars-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/stargazers
[issues-shield]: https://img.shields.io/github/issues/bansky-cl/diffusion-nlp-paper-arxiv.svg?style=for-the-badge
[issues-url]: https://github.com/bansky-cl/diffusion-nlp-paper-arxiv/issues

