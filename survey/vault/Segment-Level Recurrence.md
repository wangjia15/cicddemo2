---
title: Segment-Level Recurrence
aliases: [Segment-Level Recurrence, Segment Recurrence, Block Recurrence]
tags: [llm-memory/architecture, concept]
status: draft
---

Segment-level recurrence is the design pattern of splitting a long sequence into fixed-length segments and carrying information from one segment to the next, turning an otherwise feed-forward Transformer into a recurrent network at the granularity of whole blocks rather than single tokens. Transformer-XL introduced the canonical form: the hidden states of the previous segment are cached (with gradients stopped) and prepended as extra context when attending within the current segment, so dependencies can span segment boundaries without re-encoding the whole history [@dai2019]. Because reused states would otherwise carry inconsistent absolute positions, the pattern typically pairs with relative positional encoding. Later models vary *what* crosses the boundary: Compressive Transformers pass compressed activations [@rae2020], while the Recurrent Memory Transformer passes a handful of learned memory-token states instead of raw activations [@bulatov2022]. The shared limitation is the bounded carry: whatever crosses the segment boundary is finite in size, so information must eventually be dropped, compressed, or summarized, and very long-range exact recall remains hard. This pattern is the backbone of the recurrent-memory family of long-context Transformers.

## Related
- [[Transformer-XL]]
- [[Compressive Transformers]]
- [[Recurrent Memory Transformer]]
- [[Infini-Attention]]
- [[KV-Cache As Short-Term Memory]]
- [[MOC - Memory Architectures]]
