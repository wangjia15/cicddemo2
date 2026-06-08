---
title: Self-Attention And Quadratic Cost
aliases: [Self-Attention, Scaled Dot-Product Attention, Quadratic Attention]
tags: [llm-memory/context, concept]
status: draft
---

Self-attention is the core operation of the Transformer: each token computes query, key, and value projections and attends to every other token via scaled dot-product similarity, producing a weighted sum of values [@vaswani2017]. Because every token attends to every other token, both the time and memory cost scale as O(n^2) in sequence length n, which is the central bottleneck for treating long contexts as working memory. This quadratic cost motivates the entire line of efficient and long-context attention methods, as well as hardware-aware implementations. The mechanism itself is content-based and permutation-invariant, so position information must be injected separately through positional encodings. Limitations include the memory wall at long sequence lengths and the fact that full attention spends compute on many low-relevance token pairs.

## Related
- [[Context Window As Working Memory]]
- [[Rotary Position Embedding]]
- [[FlashAttention]]
- [[Longformer]]
- [[BigBird]]
- [[MOC - Context Memory]]
