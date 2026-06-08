---
title: Retrieval-Augmented Generation (RAG)
aliases: [RAG, Retrieval Augmented Generation]
tags: [llm-memory/retrieval, architecture]
status: draft
---

Retrieval-Augmented Generation is a general framework in which a language model's input is augmented with passages fetched from an external corpus at inference time, so generation is conditioned on retrieved evidence rather than parametric memory alone. The original RAG model [@lewis2020] pairs a dense passage retriever (DPR-style) over a Wikipedia index with a BART seq2seq generator, and proposes two variants: RAG-Sequence (one retrieved document conditions the whole output) and RAG-Token (the model can attend to different documents per token), with retriever and generator trained jointly end-to-end. RAG improves performance on knowledge-intensive tasks such as open-domain question answering and reduces hallucination by grounding outputs in retrieved text. As a paradigm, "RAG" has broadened beyond the original architecture to describe almost any retrieve-then-generate pipeline built around an LLM and a vector store. Its core advantages are updatable knowledge and attributable answers; its core failure modes stem from imperfect retrieval and the model ignoring or contradicting retrieved context.

## Related
- [[Parametric Vs Non-Parametric Memory]]
- [[Dense Passage Retrieval (DPR)]]
- [[Chunking And Embeddings]]
- [[Vector Databases And ANN Search]]
- [[REALM]]
- [[RETRO]]
- [[Atlas]]
- [[Retrieval Failure Modes And Hallucination]]
- [[Updatable Knowledge And Attribution]]
