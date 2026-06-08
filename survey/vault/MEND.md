---
title: MEND
aliases: [MEND, Model Editor Networks with Gradient Decomposition]
tags: [llm-memory/parametric-editing, method]
status: draft
---

MEND (Model Editor Networks using Gradient Decomposition) is a meta-learning approach to [[Knowledge Editing]] that trains small auxiliary networks to transform a single fine-tuning gradient into a targeted, locality-preserving weight edit [@mitchell2022mend]. The key idea is to exploit the low-rank structure of the gradient of the loss for one example with respect to a layer's weights, decomposing it so the hypernetwork can map it to a parameter update efficiently even for very large models. After this lightweight training, MEND applies fast edits at test time without the cost of locating circuits, making it usable on models with billions of parameters. It targets reliability and locality, aiming to change the edited fact and its paraphrases while leaving unrelated predictions intact, and is benchmarked on tasks like [[zsRE]] and fact editing. MEND is the canonical hypernetwork editor alongside [[KnowledgeEditor]].

## Related
- [[KnowledgeEditor]]
- [[SERAC]]
- [[Knowledge Editing]]
- [[ROME]]
- [[zsRE]]
- [[MOC - Parametric Memory and Editing]]
