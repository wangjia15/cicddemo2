---
title: FlashAttention
aliases: [FlashAttention, Flash Attention, FlashAttention-2]
tags: [llm-memory/context, method]
status: draft
---

FlashAttention is an exact attention algorithm that is IO-aware: rather than changing the math, it reorders the computation to minimize reads and writes between the GPU's slow high-bandwidth memory and fast on-chip SRAM [@dao2022flashattention]. It tiles the query, key, and value matrices, computes attention block by block, and uses online softmax with rescaling so the full attention matrix is never materialized, reducing memory from O(n^2) to O(n) and giving large wall-clock speedups. Because it is exact, it does not approximate or sparsify attention, so it complements rather than competes with methods like Longformer; it simply makes longer working-memory windows practical to train and serve. FlashAttention-2 [@dao2023flashattention2] further improves parallelism and work partitioning. Its main limitations are that it is a kernel-level optimization tied to specific hardware and that, being exact full attention, it does not reduce the fundamental quadratic compute, only the memory traffic.

## Related
- [[Self-Attention And Quadratic Cost]]
- [[Longformer]]
- [[BigBird]]
- [[Paged Attention And vLLM]]
- [[Context Window As Working Memory]]
- [[MOC - Context Memory]]
