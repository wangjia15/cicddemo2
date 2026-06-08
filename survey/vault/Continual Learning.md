---
title: Continual Learning
aliases: [Continual Learning, Lifelong Learning, Incremental Learning]
tags: [llm-memory/parametric-editing, concept]
status: draft
---

Continual learning is the setting in which a model must acquire a stream of new knowledge or tasks over time while retaining what it learned before, directly confronting [[Catastrophic Forgetting]]. Its governing challenge is the stability-plasticity dilemma: too much plasticity overwrites old knowledge, too much stability blocks new learning. Standard method families are regularization-based (penalize changes to weights deemed important, e.g. Elastic Weight Consolidation [@kirkpatrick2017]), replay/rehearsal-based (interleave stored or generated past examples), and architecture/parameter-isolation-based (allocate separate capacity per task). For large language models, continual learning manifests as keeping factual memory current, adapting to new domains, and integrating sequences of edits without regression, which is why sequential [[Knowledge Editing]] is often framed as a continual-learning problem. It provides the conceptual backdrop for why one-shot weight edits and external-memory methods like [[SERAC]] are attractive: they update knowledge while limiting interference.

## Related
- [[Catastrophic Forgetting]]
- [[Knowledge Updating Vs Forgetting]]
- [[Knowledge Editing]]
- [[SERAC]]
- [[Parametric Memory]]
- [[MOC - Parametric Memory and Editing]]
