---
title: Position Interpolation
aliases: [Position Interpolation, PI, Linear Position Interpolation]
tags: [llm-memory/context, method]
status: draft
---

Position Interpolation (PI) extends the context window of a RoPE-based model by linearly down-scaling the position indices so that inputs longer than the training length map back into the original trained range of rotary angles [@chen2023pi]. Instead of extrapolating to unseen large positions (which causes RoPE to fail), PI interpolates between trained positions, keeping attention scores in-distribution; a short fine-tuning stage (often only a few hundred steps) then adapts the model to the denser positions. This expanded LLaMA models from 2k to up to 32k tokens cheaply while preserving performance at the original length. The core limitation is that uniform interpolation compresses high-frequency rotary dimensions that encode fine local order, which can blur short-range positional resolution; this shortcoming motivated NTK-aware scaling and [[YaRN]], which interpolate non-uniformly across frequencies.

## Related
- [[Rotary Position Embedding]]
- [[YaRN]]
- [[Length Generalization And Extrapolation]]
- [[Context Window As Working Memory]]
- [[MOC - Context Memory]]
