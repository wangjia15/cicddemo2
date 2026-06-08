---
title: Dense Passage Retrieval (DPR)
aliases: [DPR, Dense Passage Retrieval, Dense Retrieval]
tags: [llm-memory/retrieval, method]
status: draft
---

Dense Passage Retrieval (DPR) is a dense retrieval method that learns to embed questions and passages into a shared vector space so that relevant pairs have high inner-product similarity [@karpukhin2020]. It uses a dual-encoder (two BERT encoders, one for queries and one for passages) trained with a contrastive objective using in-batch negatives and hard negatives, so retrieval reduces to nearest-neighbor search over precomputed passage embeddings. DPR substantially outperformed traditional sparse lexical retrieval (BM25/TF-IDF) on open-domain question answering by capturing semantic rather than purely lexical matches. It became the standard retriever component plugged into downstream readers and generators, including RAG [@lewis2020]. The embeddings are typically indexed with a vector database and approximate nearest neighbor search for scalability. Limitations include sensitivity to training negatives, weaker handling of rare entities and exact-match terms where lexical methods still help, and the cost of re-encoding the corpus when the encoder changes.

## Related
- [[Retrieval-Augmented Generation (RAG)]]
- [[Vector Databases And ANN Search]]
- [[Chunking And Embeddings]]
- [[REALM]]
- [[Atlas]]
- [[Parametric Vs Non-Parametric Memory]]
