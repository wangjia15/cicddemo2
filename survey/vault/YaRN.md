---
title: YaRN
aliases: [YaRN, Yet another RoPE extensioN, NTK-aware Scaling]
tags: [llm-memory/context, method]
status: draft
---

YaRN (Yet another RoPE extensioN method) is an efficient context-extension technique that improves on plain position interpolation by scaling RoPE frequencies non-uniformly: it interpolates low-frequency (long-wavelength) dimensions while leaving high-frequency dimensions closer to their original values, following NTK-aware reasoning so fine local position resolution is preserved [@peng2023yarn]. It also introduces an attention temperature adjustment to keep the softmax distribution well-scaled at longer lengths. YaRN reaches much longer context windows (e.g., extending LLaMA to 64k-128k tokens) with far less fine-tuning data and fewer training steps than linear interpolation. Its limitations mirror other extension methods: the gains rely on some continued fine-tuning, very long contexts still strain effective retrieval, and the chosen scaling hyperparameters are partly empirical. YaRN is the refined successor to [[Position Interpolation]] within the [[Rotary Position Embedding]] family.

## Related
- [[Position Interpolation]]
- [[Rotary Position Embedding]]
- [[Length Generalization And Extrapolation]]
- [[Context Window As Working Memory]]
- [[MOC - Context Memory]]
