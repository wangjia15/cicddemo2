---
title: Retrieval Failure Modes and Hallucination
aliases: [Retrieval Errors, Hallucination, RAG Failure Modes]
tags: [llm-memory/retrieval, concept]
status: draft
---

Retrieval-augmented systems fail in characteristic ways even though they reduce hallucination overall. Retrieval errors occur when the index lacks the needed information, when the embedding similarity surfaces irrelevant or distracting passages, or when good evidence exists but is ranked below the cutoff (recall failures). Even with correct evidence retrieved, the generator may ignore the context and fall back on parametric memory, or it may misread or over-generalize the passages, producing claims unsupported by or contradicting the retrieved text. Surveys of hallucination in LLMs distinguish such faithfulness/grounding failures from factuality failures and note that retrieval can introduce conflicts between parametric and retrieved knowledge [@ji2023]. Long or noisy retrieved contexts can also degrade output via distraction and "lost in the middle" position effects. Mitigations include better retrievers and rerankers, careful chunking, context filtering, citation/grounding checks, and training the model to abstain when evidence is insufficient. These failure modes are the principal limitations balancing the updatability and attribution benefits of non-parametric memory.

## Related
- [[Retrieval-Augmented Generation (RAG)]]
- [[Updatable Knowledge And Attribution]]
- [[Chunking And Embeddings]]
- [[Dense Passage Retrieval (DPR)]]
- [[Parametric Vs Non-Parametric Memory]]
