---
title: Knowledge Neurons
aliases: [Knowledge Neurons, KN]
tags: [llm-memory/parametric-editing, method]
status: draft
---

Knowledge neurons are individual neurons in the feed-forward layers of a pretrained Transformer that Dai et al. identified as responsible for expressing specific relational facts [@dai2022]. Using an integrated-gradients attribution over FFN intermediate activations, the method scores how much each neuron contributes to predicting a fact's object given cloze-style prompts (as in [[LAMA Probe]]), isolating a small set of neurons tied to that fact. The authors showed that suppressing or amplifying these neurons predictably weakens or strengthens the corresponding fact, and that crudely editing them can update or erase knowledge without fine-tuning. This work is an early demonstration that parametric factual memory is partly localizable at neuron granularity, complementing the layer-level [[FFN As Key-Value Memory]] view and the causal-tracing localization used by [[ROME]]. It sits between interpretability and [[Knowledge Editing]].

## Related
- [[FFN As Key-Value Memory]]
- [[ROME]]
- [[Knowledge Editing]]
- [[LAMA Probe]]
- [[Parametric Memory]]
- [[MOC - Parametric Memory and Editing]]
