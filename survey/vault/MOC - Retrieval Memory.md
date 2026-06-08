---
title: MOC - Retrieval Memory
aliases: [Retrieval Memory MOC, External Memory MOC, Non-Parametric Memory MOC]
tags: [llm-memory/retrieval, moc]
status: draft
---

# Map of Content: External / Retrieval Memory

This cluster covers **non-parametric memory** for large language models: knowledge held in an external, retrievable store rather than baked into model weights. The organizing idea is to separate what the model *knows in its parameters* from what it can *look up at inference time*, then retrieve relevant evidence and condition generation on it.

## Framing
- [[Parametric Vs Non-Parametric Memory]] — the core distinction underlying the whole cluster (see also [[Parametric Memory]] in the parametric-editing cluster).
- [[Updatable Knowledge And Attribution]] — the main advantages of external memory.
- [[Retrieval Failure Modes And Hallucination]] — the main limitations and how they arise.

## The Paradigm
- [[Retrieval-Augmented Generation (RAG)]] — the retrieve-then-generate framework and its original architecture.

## Foundational Retrieval-Augmented Language Models
- [[kNN-LM]] — token-level nearest-neighbor interpolation over a datastore.
- [[REALM]] — learned retrieval integrated into pretraining.
- [[RETRO]] — trillion-token database with chunked cross-attention.
- [[Atlas]] — sample-efficient retrieval-augmented few-shot learner.

## Retrieval Machinery
- [[Dense Passage Retrieval (DPR)]] — dual-encoder dense retrieval that beat sparse methods.
- [[Vector Databases And ANN Search]] — FAISS, HNSW, MIPS: making large-scale similarity search feasible.
- [[Chunking And Embeddings]] — preparing a corpus into retrievable, embedded units.

## Suggested Reading Order
1. [[Parametric Vs Non-Parametric Memory]]
2. [[Retrieval-Augmented Generation (RAG)]]
3. [[Dense Passage Retrieval (DPR)]] → [[Chunking And Embeddings]] → [[Vector Databases And ANN Search]]
4. [[kNN-LM]] → [[REALM]] → [[RETRO]] → [[Atlas]]
5. [[Updatable Knowledge And Attribution]] and [[Retrieval Failure Modes And Hallucination]]
