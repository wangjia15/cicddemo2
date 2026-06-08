---
title: BigBird
aliases: [Big Bird, BigBird]
tags: [llm-memory/context, architecture]
status: draft
---

BigBird is a sparse-attention Transformer that approximates full attention with a linear-cost pattern built from three components: local window attention, a set of global tokens, and a number of random attention connections per token [@zaheer2020bigbird]. The random links give the sparse attention graph small-world connectivity so information can propagate between any two positions in a few layers, and the authors prove BigBird is a universal approximator of sequence functions and Turing complete, preserving the theoretical power of full attention. This enables handling sequences roughly eight times longer than standard BERT on similar hardware, useful for long-document and genomics tasks. Limitations include that the theoretical guarantees rely on global tokens, the random pattern complicates efficient hardware implementation, and very long-range exact dependencies can still be lossy. BigBird is the random-plus-structured counterpart to [[Longformer]].

## Related
- [[Longformer]]
- [[Self-Attention And Quadratic Cost]]
- [[FlashAttention]]
- [[Context Window As Working Memory]]
- [[MOC - Context Memory]]
