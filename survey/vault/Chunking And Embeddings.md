---
title: Chunking and Embeddings
aliases: [Chunking, Embeddings, Text Chunking, Document Splitting]
tags: [llm-memory/retrieval, concept]
status: draft
---

Before a corpus can serve as non-parametric memory, documents are split into chunks and each chunk is converted into a dense embedding vector for indexing. Chunking strategy (fixed token windows, sentence or paragraph boundaries, semantic splitting, and overlap between chunks) controls the granularity of retrieval: chunks that are too large dilute relevance and waste context window, while chunks that are too small fragment meaning and lose context needed to answer. Embeddings are produced by a text encoder (e.g., a dual-encoder like DPR [@karpukhin2020], Contriever, or a general sentence/text embedding model) so that semantically similar text lands nearby in vector space. The quality of retrieval is bounded by both embedding quality and chunking choices, and a query embedding is compared against chunk embeddings using approximate nearest neighbor search. Practical pipelines also attach metadata to chunks for filtering and attribution. Poor chunking is a common, often-overlooked source of retrieval failure in RAG systems.

## Related
- [[Dense Passage Retrieval (DPR)]]
- [[Vector Databases And ANN Search]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[Retrieval Failure Modes And Hallucination]]
