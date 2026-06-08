---
title: Atlas
aliases: [Atlas, Atlas retrieval-augmented model]
tags: [llm-memory/retrieval, architecture]
status: draft
---

Atlas is a retrieval-augmented encoder-decoder language model designed for strong few-shot learning on knowledge-intensive tasks [@izacard2022]. It pairs a Contriever-based dense retriever with a Fusion-in-Decoder (FiD) reader, and demonstrates that careful joint training of retriever and reader lets a relatively small model (e.g., 11B parameters) match or exceed much larger parametric models on tasks like open-domain QA and fact checking with very few training examples. Atlas studies several retriever training objectives (e.g., attention distillation and perplexity-based losses) that let the language modeling signal supervise retrieval without explicit relevance labels. Like other retrieval-augmented models, its knowledge can be updated by editing the index, and it supports attribution to retrieved documents. Its main contribution is showing retrieval augmentation is highly sample-efficient; limitations include the cost of jointly training and maintaining the retriever and index.

## Related
- [[Retrieval-Augmented Generation (RAG)]]
- [[REALM]]
- [[RETRO]]
- [[Dense Passage Retrieval (DPR)]]
- [[Updatable Knowledge And Attribution]]
