---
title: Updatable Knowledge and Attribution
aliases: [Updatable Knowledge, Attribution, Source Grounding, Knowledge Editing via Retrieval]
tags: [llm-memory/retrieval, concept]
status: draft
---

Two central advantages of external/retrieval memory over purely parametric memory are updatability and attribution. Because knowledge lives in an external index rather than the weights, it can be added, removed, or corrected by editing the corpus without retraining the model, addressing knowledge staleness and the high cost of re-pretraining; RAG explicitly highlighted this hot-swappable knowledge property [@lewis2020]. Attribution means the model can cite the specific retrieved passages that grounded its answer, improving transparency, verifiability, and user trust, and enabling factuality checks against sources. These properties make retrieval-augmented systems attractive for fast-moving or proprietary domains where facts change frequently. However, the guarantees are only as good as the retrieval: if the wrong passages are retrieved, attribution can be misleading, and the model may still generate claims unsupported by the cited text. Thus updatability and attribution mitigate, but do not eliminate, hallucination and factual error.

## Related
- [[Parametric Vs Non-Parametric Memory]]
- [[Retrieval-Augmented Generation (RAG)]]
- [[Retrieval Failure Modes And Hallucination]]
- [[Atlas]]
