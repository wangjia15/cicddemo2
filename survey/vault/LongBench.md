---
title: LongBench
aliases: [LongBench, LongBench v2]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

LongBench is a bilingual (English and Chinese), multi-task benchmark by Bai et al. for evaluating long-context understanding in language models on realistic tasks rather than synthetic probes [@bai2024]. It spans six task categories — single-document QA, multi-document QA, summarization, few-shot learning, synthetic tasks, and code completion — across 21 datasets, with average input lengths typically in the thousands to tens of thousands of tokens. To keep evaluation cheap and automatic, all tasks use standardized output formats and metrics (e.g. F1, ROUGE, accuracy, edit similarity), and a compressed "LongBench-E" subset offers a balanced length distribution for studying performance versus input length. Its emphasis on naturalistic, downstream tasks distinguishes it from purely synthetic suites such as [[RULER]] and the retrieval-only [[Needle In A Haystack]]. A later LongBench v2 [@bai2025] raises difficulty toward deep reasoning over very long, realistic contexts.

## Related
- [[ZeroSCROLLS]]
- [[InfiniteBench]]
- [[RULER]]
- [[Needle In A Haystack]]
- [[MOC - Evaluation and Benchmarks]]
