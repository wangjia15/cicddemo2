---
title: REALM
aliases: [REALM, Retrieval-Augmented Language Model Pre-Training]
tags: [llm-memory/retrieval, architecture]
status: draft
---

REALM (Retrieval-Augmented Language Model pre-training) is one of the first methods to integrate a learned retriever into language model pretraining itself [@guu2020]. During masked language modeling, REALM retrieves documents from a corpus (e.g., Wikipedia) using a learned neural knowledge retriever, then conditions the masked-token predictions on the retrieved text, so the retriever is trained by backpropagating the language modeling signal. To make retrieval over a large corpus tractable during training, REALM uses Maximum Inner Product Search (MIPS) with an index of document embeddings that is asynchronously refreshed as the encoder updates. After pretraining, REALM is fine-tuned for open-domain question answering, where it outperformed prior parametric-only models. Its key contribution is showing that retrieval can be learned end-to-end as part of pretraining rather than bolted on afterward. The main costs are the engineering complexity of keeping the index in sync and the expense of re-encoding the corpus.

## Related
- [[Retrieval-Augmented Generation (RAG)]]
- [[Dense Passage Retrieval (DPR)]]
- [[Parametric Vs Non-Parametric Memory]]
- [[Atlas]]
- [[Vector Databases And ANN Search]]
