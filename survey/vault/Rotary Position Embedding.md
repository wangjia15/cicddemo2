---
title: Rotary Position Embedding
aliases: [RoPE, Rotary Embeddings]
tags: [llm-memory/context, method]
status: draft
---

Rotary Position Embedding (RoPE) encodes absolute position by rotating the query and key vectors by an angle proportional to their position before computing attention [@su2021roformer]. Because the dot product of two rotated vectors depends only on their relative offset, RoPE injects relative position information directly into the attention score while using an absolute formulation, giving smooth decay of attention with distance. RoPE has become the dominant positional encoding in modern LLMs (e.g., LLaMA, PaLM) because it composes cleanly with attention and supports some length extrapolation. Its core limitation is that models trained at one context length degrade when run far beyond it, since high-frequency rotary components see out-of-distribution angles; this motivates extension methods like position interpolation and YaRN. RoPE is the natural baseline that ALiBi, NTK-aware scaling, and YaRN build on or contrast with.

## Related
- [[ALiBi]]
- [[Position Interpolation]]
- [[YaRN]]
- [[Length Generalization And Extrapolation]]
- [[Self-Attention And Quadratic Cost]]
- [[MOC - Context Memory]]
