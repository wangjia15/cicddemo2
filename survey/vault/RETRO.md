---
title: RETRO
aliases: [RETRO, Retrieval-Enhanced Transformer]
tags: [llm-memory/retrieval, architecture]
status: draft
---

RETRO (Retrieval-Enhanced Transformer) is an autoregressive language model that retrieves from a very large text database (trillions of tokens) and fuses the retrieved neighbors into generation through a dedicated chunked cross-attention mechanism [@borgeaud2022]. Input sequences are split into chunks; for each chunk, the model retrieves nearest-neighbor chunks (with their continuations) from the database using a frozen BERT embedding and approximate nearest neighbor search, then attends to them via chunked cross-attention. RETRO showed that a relatively small model with retrieval can match the performance of models an order of magnitude larger in parameters, effectively offloading factual memorization to the non-parametric database. Because the retrieval database is decoupled from the weights, knowledge can be updated by changing the database without retraining the model. Limitations include the substantial infrastructure required to build and serve a trillion-token index and complexity in the chunked cross-attention design.

## Related
- [[Retrieval-Augmented Generation (RAG)]]
- [[kNN-LM]]
- [[Memorizing Transformers]]
- [[Atlas]]
- [[Chunking And Embeddings]]
- [[Vector Databases And ANN Search]]
- [[Parametric Vs Non-Parametric Memory]]
