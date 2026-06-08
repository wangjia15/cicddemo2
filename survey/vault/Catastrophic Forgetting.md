---
title: Catastrophic Forgetting
aliases: [Catastrophic Forgetting, Catastrophic Interference]
tags: [llm-memory/parametric-editing, concept]
status: draft
---

Catastrophic forgetting is the tendency of a neural network to lose previously acquired knowledge when trained on new data or tasks, because gradient updates overwrite the weights that encoded the old information [@mccloskey1989]. It is the central obstacle to updating parametric memory: naive fine-tuning to insert a new fact, or to learn a new task, can degrade unrelated capabilities, which is why [[Knowledge Editing]] methods explicitly optimize for locality and specificity. Classic mitigations from continual learning include regularization that protects important weights, such as Elastic Weight Consolidation [@kirkpatrick2017], replay of past examples, and parameter-isolation or modular approaches. In large language models the same pressure appears during instruction tuning and domain adaptation, where new training can erode pretrained knowledge. Managing the trade-off between plasticity (learning the new) and stability (retaining the old) is the stability-plasticity dilemma at the heart of [[Continual Learning]].

## Related
- [[Continual Learning]]
- [[Knowledge Editing]]
- [[Knowledge Updating Vs Forgetting]]
- [[Parametric Memory]]
- [[MOC - Parametric Memory and Editing]]
