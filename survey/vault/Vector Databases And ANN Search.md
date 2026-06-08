---
title: Vector Databases and ANN Search
aliases: [Vector Database, ANN, Approximate Nearest Neighbor, FAISS, HNSW, MIPS]
tags: [llm-memory/retrieval, concept]
status: draft
---

A vector database stores high-dimensional embeddings and answers similarity queries by finding the vectors closest to a query vector, which underpins the non-parametric memory of retrieval-augmented systems. Exact nearest-neighbor search is too slow at scale, so these systems use Approximate Nearest Neighbor (ANN) search, trading a small amount of recall for large speed gains. FAISS is a widely used library for efficient similarity search and clustering of dense vectors, supporting GPU acceleration and many index types (flat, IVF, product quantization) [@johnson2019]. HNSW (Hierarchical Navigable Small World) is a graph-based ANN index that builds a multi-layer proximity graph enabling fast logarithmic-style greedy search with high recall [@malkov2018]. Retrieval based on inner-product similarity is often called Maximum Inner Product Search (MIPS), used by methods like REALM. These indexes make retrieval over millions to billions of passages feasible at inference time, but introduce trade-offs between recall, latency, memory footprint, and index build/update cost.

## Related
- [[Dense Passage Retrieval (DPR)]]
- [[Chunking And Embeddings]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[kNN-LM]]
- [[RETRO]]
- [[REALM]]
