---
title: InfiniteBench
aliases: [InfiniteBench, ∞Bench, InfinityBench]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

InfiniteBench is a benchmark by Zhang et al. built to evaluate language models on contexts beyond 100K tokens, where average input length far exceeds earlier long-context suites [@zhang2024]. It contains twelve tasks across English and Chinese spanning retrieval, long-book and long-dialogue question answering, summarization, novel-character tracking, mathematical reasoning over long inputs, and code debugging, mixing realistic and synthetic constructions. The design goal is to probe whether models can genuinely process, recall, and reason over extremely long inputs rather than just locate an isolated needle, so several tasks require aggregation and multi-step reasoning. Results showed that even leading long-context models degrade substantially at the 100K+ regime, leaving large headroom. It pushes the length frontier past [[LongBench]] and [[ZeroSCROLLS]] while remaining more naturalistic than the fully synthetic [[RULER]].

## Related
- [[LongBench]]
- [[ZeroSCROLLS]]
- [[RULER]]
- [[Needle In A Haystack]]
- [[MOC - Evaluation and Benchmarks]]
