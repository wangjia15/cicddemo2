---
title: Length Generalization And Extrapolation
aliases: [Length Extrapolation, Length Generalization]
tags: [llm-memory/context, concept]
status: draft
---

Length generalization is the ability of a model trained on sequences up to some length to behave correctly on longer sequences at inference time, effectively expanding its usable working memory without retraining. The phenomenon is governed largely by how positional information is encoded: out-of-distribution positions produce attention scores the model never saw during training, causing perplexity to spike. ALiBi was explicitly designed for extrapolation via its distance-linear bias [@press2021alibi], whereas vanilla [[Rotary Position Embedding]] extrapolates poorly and motivated interpolation-based fixes. Extension techniques such as position interpolation [@chen2023pi] and YaRN [@peng2023yarn] rescale or reparameterize positions so longer inputs map back into the trained range. A key limitation is that extrapolation often preserves fluency (low perplexity) without preserving the ability to actually retrieve distant facts, so length generalization and effective long-context reasoning are distinct goals.

## Related
- [[ALiBi]]
- [[Rotary Position Embedding]]
- [[Position Interpolation]]
- [[YaRN]]
- [[Lost In The Middle]]
- [[MOC - Context Memory]]
