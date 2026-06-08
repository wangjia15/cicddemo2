---
title: kNN-LM
aliases: [kNN-LM, Nearest Neighbor Language Model, k-Nearest-Neighbor Language Model]
tags: [llm-memory/retrieval, method]
status: draft
---

kNN-LM augments a pretrained autoregressive language model with a nearest-neighbor retrieval mechanism over a datastore of cached context-representation/next-token pairs [@khandelwal2020]. At inference, the current context's hidden representation is used as a query to find the k most similar contexts in the datastore (via approximate nearest neighbor search over key vectors), and the empirical distribution of their next tokens is interpolated with the base LM's softmax distribution. This lets the model "memorize" rare patterns and long-tail facts without updating any parameters, improving perplexity, and the datastore can be expanded or swapped to adapt to new domains without retraining. Crucially, the retrieval operates at the token level over the LM's own representation space, rather than retrieving documents to read. Limitations include the large memory and storage footprint of the datastore and the latency of per-token similarity search. It is a foundational demonstration that explicit non-parametric memory can complement parametric memory.

## Related
- [[Parametric Vs Non-Parametric Memory]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[RETRO]]
- [[Memorizing Transformers]]
- [[Vector Databases And ANN Search]]
- [[Chunking And Embeddings]]
