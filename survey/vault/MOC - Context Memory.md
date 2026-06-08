---
title: MOC - Context Memory
aliases: [Context Memory MOC, Implicit Memory MOC, Working Memory MOC]
tags: [llm-memory/context, moc]
status: draft
---

# Map of Content: Implicit / Context Memory

This cluster covers the **implicit, in-context memory** of large language models: information the model holds not in its weights but in the live span of tokens it can attend to. The organizing idea is the context window as a finite, volatile *working memory*, and the bulk of the work here is about making that window larger, cheaper, or better managed — through positional encodings, efficient attention, KV-cache management, and context-extension methods.

## Framing
- [[Context Window As Working Memory]] — the finite, ephemeral token span that acts as the model's working memory and the anchor for this whole cluster.
- [[Self-Attention And Quadratic Cost]] — why context is expensive: attention scales as O(n^2) in sequence length, the bottleneck everything else attacks.
- [[Length Generalization And Extrapolation]] — running trained models on longer sequences than they saw, and why fluency does not imply recall.
- [[Lost In The Middle]] — the positional bias showing a big window is not the same as usable working memory.

## Positional Encodings (length generalization)
- [[Rotary Position Embedding]] — RoPE: rotates queries/keys so dot products encode relative position; the dominant scheme in modern LLMs.
- [[ALiBi]] — adds a distance-linear attention bias instead of embeddings, designed for length extrapolation.

## Efficient / Long-Context Attention
- [[Longformer]] — sparse local-window plus global-token attention that scales linearly.
- [[BigBird]] — local + global + random sparse attention with universal-approximation guarantees.
- [[FlashAttention]] — IO-aware exact attention that cuts memory traffic, not the math, to make long windows practical.

## KV-Cache As Short-Term Memory (and its management)
- [[KV-Cache As Short-Term Memory]] — the cached keys/values that are the concrete substrate of context memory, and the binding serving constraint.
- [[StreamingLLM And Attention Sinks]] — keep initial "sink" tokens plus a recent window for unbounded streaming at fixed cache size.
- [[H2O Heavy Hitter Oracle]] — evict all but attention "heavy hitters" plus recent tokens to shrink the cache adaptively.
- [[Paged Attention And vLLM]] — OS-style paging of the cache to kill fragmentation and raise serving throughput.

## Context Extension Methods
- [[Position Interpolation]] — linearly rescale RoPE position indices back into the trained range, plus light fine-tuning.
- [[YaRN]] — NTK-aware, frequency-dependent RoPE rescaling that extends context with less fine-tuning than plain interpolation.

## Suggested Reading Order
1. [[Context Window As Working Memory]] → [[Self-Attention And Quadratic Cost]]
2. [[Rotary Position Embedding]] → [[ALiBi]] → [[Length Generalization And Extrapolation]]
3. [[Longformer]] → [[BigBird]] → [[FlashAttention]]
4. [[KV-Cache As Short-Term Memory]] → [[StreamingLLM And Attention Sinks]] → [[H2O Heavy Hitter Oracle]] → [[Paged Attention And vLLM]]
5. [[Position Interpolation]] → [[YaRN]] → [[Lost In The Middle]]
