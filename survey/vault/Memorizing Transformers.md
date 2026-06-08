---
title: Memorizing Transformers
aliases: [Memorizing Transformer, kNN-augmented Transformer]
tags: [llm-memory/architecture, architecture]
status: draft
---

Memorizing Transformers give a Transformer access to a large, non-differentiable external memory of past key-value pairs that is queried with approximate k-nearest-neighbor (kNN) lookup at one attention layer [@wu2022]. As the model processes a long document, the keys and values of previous tokens are stored in a growing memory bank; at the designated layer each query attends both to the local context (standard attention) and to the top-k most similar keys retrieved from memory, with a learned gate blending the two. Crucially the memory is not back-propagated through and can hold tens of thousands to hundreds of thousands of past tokens, so the model can recall specific facts and rare tokens seen far earlier without retraining, and memory can even be extended at inference time. This is effectively retrieval over the model's own activations, bridging recurrent memory and retrieval-augmented methods. Limitations include the cost and engineering of maintaining and searching a large kNN index, staleness of stored keys as the model's representations drift, and benefits that concentrate on memorization-heavy tasks rather than general reasoning.

## Related
- [[Transformer-XL]]
- [[End-to-End Memory Networks]]
- [[Content-Based Addressing]]
- [[Infini-Attention]]
- [[Parametric Vs Non-Parametric Memory]]
- [[MOC - Memory Architectures]]
