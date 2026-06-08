---
title: KV-Cache As Short-Term Memory
aliases: [KV Cache, Key-Value Cache, KV-Cache]
tags: [llm-memory/context, concept]
status: draft
---

During autoregressive generation, a Transformer caches the key and value vectors of all previously processed tokens so that each new token only computes attention against the cache rather than recomputing the entire prefix; this KV-cache is the concrete substrate of the model's short-term context memory. Its size grows linearly with sequence length, number of layers, and number of attention heads, so for long contexts and large batches the KV-cache, not the model weights, becomes the dominant memory consumer and the binding constraint on serving throughput. This pressure drives a family of management techniques: eviction policies that keep only important entries (H2O), structural patterns that retain initial tokens (StreamingLLM / attention sinks), and memory allocators that reduce fragmentation (paged attention in vLLM). The central limitation is the tension between retaining enough cache for accurate long-range recall and shrinking it enough to fit memory and stay fast. The KV-cache is thus the operational form of the working memory described in [[Context Window As Working Memory]].

## Related
- [[StreamingLLM And Attention Sinks]]
- [[H2O Heavy Hitter Oracle]]
- [[Paged Attention And vLLM]]
- [[Context Window As Working Memory]]
- [[Self-Attention And Quadratic Cost]]
- [[MOC - Context Memory]]
