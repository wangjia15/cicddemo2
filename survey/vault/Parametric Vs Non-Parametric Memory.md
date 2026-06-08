---
title: Parametric vs Non-Parametric Memory
aliases: [Parametric Memory, Non-Parametric Memory, Implicit vs Explicit Memory]
tags: [llm-memory/retrieval, concept]
status: draft
---

Parametric memory is knowledge stored implicitly in the weights of a neural network, learned during pretraining and accessed by a forward pass; it is compact and fast but opaque, hard to update, and prone to staleness and hallucination. Non-parametric memory is knowledge held explicitly in an external store (a text corpus, document index, or vector database) that the model retrieves from at inference time. The distinction was made central by RAG [@lewis2020], which combined a parametric seq2seq generator with a non-parametric Wikipedia index accessed via dense retrieval. Non-parametric memory can be edited, swapped, or grown without retraining, and supports source attribution, while parametric memory excels at fluent generalization and reasoning. Most retrieval-augmented systems are hybrids: a parametric model conditioned on non-parametric retrieved evidence. This separation is the organizing principle of the External / Retrieval Memory cluster.

## Related
- [[Parametric Memory]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[kNN-LM]]
- [[REALM]]
- [[Updatable Knowledge And Attribution]]
- [[MOC - Retrieval Memory]]
