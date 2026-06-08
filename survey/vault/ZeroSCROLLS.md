---
title: ZeroSCROLLS
aliases: [ZeroSCROLLS, Zero-Shot SCROLLS, SCROLLS]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

ZeroSCROLLS is a zero-shot benchmark by Shaham et al. for natural-language understanding over long texts, evaluating models without any task-specific fine-tuning [@shaham2023]. It builds on the earlier supervised SCROLLS suite [@shaham2022] and adds new tasks, covering long-document summarization, question answering over lengthy contexts, query-based summarization, and aggregation tasks such as sentiment aggregation and sorting that require reasoning over the whole input rather than a single span. By being zero-shot, it specifically targets the in-context long-text abilities of instruction-tuned and very large models, with a public leaderboard for comparison. ZeroSCROLLS emphasizes naturalistic documents (stories, reports, scientific articles, transcripts) at lengths of several thousand to tens of thousands of tokens. It complements synthetic stress tests like [[RULER]] and [[Needle In A Haystack]] and overlaps in spirit with [[LongBench]] and [[InfiniteBench]].

## Related
- [[LongBench]]
- [[InfiniteBench]]
- [[RULER]]
- [[Needle In A Haystack]]
- [[MOC - Evaluation and Benchmarks]]
