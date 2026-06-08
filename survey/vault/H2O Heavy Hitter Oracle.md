---
title: H2O Heavy Hitter Oracle
aliases: [H2O, Heavy Hitter Oracle, Heavy-Hitter Oracle]
tags: [llm-memory/context, method]
status: draft
---

H2O (Heavy-Hitter Oracle) is a KV-cache eviction policy that shrinks the cache by keeping only the most important tokens, observing that a small set of "heavy hitter" tokens accounts for the majority of attention mass and that removing them sharply degrades quality [@zhang2023h2o]. It maintains a budget combining these heavy hitters (identified from accumulated attention scores) with a window of recent tokens, and greedily evicts the rest, formulated as a dynamic submodular eviction problem. This can cut KV-cache memory substantially while largely preserving generation quality, raising serving throughput. Compared to StreamingLLM's fixed positional sinks, H2O selects tokens by learned attention importance, making it more content-adaptive. Its limitation is that attention-score-based importance is a heuristic computed greedily, so it can still evict tokens that matter for later queries, and tracking scores adds bookkeeping overhead.

## Related
- [[KV-Cache As Short-Term Memory]]
- [[StreamingLLM And Attention Sinks]]
- [[Paged Attention And vLLM]]
- [[MOC - Context Memory]]
