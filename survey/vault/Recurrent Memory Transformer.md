---
title: Recurrent Memory Transformer
aliases: [RMT, Recurrent Memory Transformers]
tags: [llm-memory/architecture, architecture]
status: draft
---

The Recurrent Memory Transformer (RMT) adds a small set of dedicated learnable "memory" tokens to the input of an otherwise standard Transformer and passes the memory token states from one segment to the next, turning the Transformer into a recurrent network at the segment level [@bulatov2022]. Special memory tokens are prepended (read memory) and appended (write memory) to each segment; after processing a segment, the output states of the write-memory tokens become the read-memory tokens fed into the next segment, so information is summarized into a fixed-width memory and carried forward without changing the base attention mechanism. Because only a few vectors are passed between segments, RMT keeps per-segment cost bounded while in principle allowing information to flow across very many segments, and follow-up work scaled this to inputs of over a million tokens by recurrently processing many segments [@bulatov2023]. Its core limitation is the tight information bottleneck: all cross-segment context must be squeezed through the small fixed number of memory tokens, which can lose detail over long horizons, and training across many recurrent steps can be unstable. RMT exemplifies summarizing past context into a compact learned state rather than caching raw activations.

## Related
- [[Transformer-XL]]
- [[Compressive Transformers]]
- [[Infini-Attention]]
- [[Memory Compression]]
- [[Segment-Level Recurrence]]
- [[MOC - Memory Architectures]]
