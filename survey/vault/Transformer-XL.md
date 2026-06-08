---
title: Transformer-XL
aliases: [Transformer XL, TransformerXL]
tags: [llm-memory/architecture, architecture]
status: draft
---

Transformer-XL introduces segment-level recurrence into the Transformer to extend the effective context beyond a single fixed-length segment [@dai2019]. During training the hidden states computed for the previous segment are cached and reused (with stopped gradient) as an extended memory when processing the current segment, so information can propagate across segment boundaries and the model captures dependencies far longer than the segment length. To make this caching consistent it replaces absolute positional encodings with a relative positional encoding, since reused states from a previous segment would otherwise carry conflicting absolute positions. The result is longer-range modeling and much faster evaluation, because previous computations are reused rather than recomputed for each shifted window. Its main limitations are that the cached memory is a fixed-size sliding window of raw past activations that are eventually discarded, so context length is still bounded by cache size and old information is simply dropped rather than compressed or retrieved. This "recurrence over cached states" idea is the foundation for Compressive Transformers, the Recurrent Memory Transformer, and Memorizing Transformers.

## Related
- [[Compressive Transformers]]
- [[Recurrent Memory Transformer]]
- [[Memorizing Transformers]]
- [[KV-Cache As Short-Term Memory]]
- [[Segment-Level Recurrence]]
- [[MOC - Memory Architectures]]
