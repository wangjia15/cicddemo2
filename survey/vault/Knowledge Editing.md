---
title: Knowledge Editing
aliases: [Model Editing, Knowledge Editing, Fact Editing, KE]
tags: [llm-memory/parametric-editing, concept]
status: draft
---

Knowledge editing is the task of making targeted changes to a model's parametric memory updating, inserting, or erasing specific facts without full retraining and without degrading unrelated behavior. A good edit is evaluated on reliability (the new fact is recalled), generalization (paraphrases and logically entailed queries also change), and locality/specificity (unrelated facts and skills are preserved), often with a portability dimension for downstream reasoning. Approaches fall into broad families: locate-then-edit methods that compute closed-form weight updates to MLP layers ([[ROME]], [[MEMIT]]); meta-learning / hypernetwork editors that learn to predict weight changes ([[MEND]], [[KnowledgeEditor]]); memory-based methods that store edits externally and route to them ([[SERAC]]); and additive parameter methods. Standard benchmarks include [[CounterFact]] and [[zsRE]]. The core tension is editing efficacy versus avoiding [[Catastrophic Forgetting]] of the rest of the model's knowledge.

## Related
- [[ROME]]
- [[MEMIT]]
- [[MEND]]
- [[KnowledgeEditor]]
- [[SERAC]]
- [[Knowledge Neurons]]
- [[Knowledge Updating Vs Forgetting]]
- [[CounterFact]]
- [[zsRE]]
- [[MOC - Parametric Memory and Editing]]
