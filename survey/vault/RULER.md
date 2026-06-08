---
title: RULER
aliases: [RULER, What's the Real Context Size of Your Long-Context Language Models]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

RULER is a synthetic benchmark by Hsieh et al. designed to measure the "real" effective context length of long-context language models with adjustable sequence lengths and task complexity [@hsieh2024]. It generalizes the simple [[Needle In A Haystack]] retrieval test into four task categories: multi-needle and multi-key/multi-value retrieval, multi-hop tracing (variable tracking across the context), aggregation (e.g. common/frequent-word extraction), and long-context question answering. Because the data is generated programmatically, RULER can scale a task to arbitrary lengths while controlling difficulty, avoiding contamination from pretraining data. Its key finding is that many models claiming very large context windows maintain accuracy only up to a fraction of their advertised length, so RULER reports an effective context length at which performance stays above a threshold. It is a much stronger probe of long-context behavior than single-needle retrieval and complements naturalistic suites like [[LongBench]] and [[InfiniteBench]].

## Related
- [[Needle In A Haystack]]
- [[LongBench]]
- [[InfiniteBench]]
- [[Long Range Arena]]
- [[Context Window As Working Memory]]
- [[MOC - Evaluation and Benchmarks]]
