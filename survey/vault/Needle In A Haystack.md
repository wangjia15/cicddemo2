---
title: Needle In A Haystack
aliases: [Needle In A Haystack, NIAH, Passkey Retrieval, NeedleInAHaystack]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

Needle-in-a-Haystack (NIAH) is a popular stress test for long-context language models that inserts a single piece of information (the "needle") at a controlled depth inside a long distractor document (the "haystack") and then asks the model to retrieve it. By sweeping the needle's position across many context depths and the total context across many lengths, it produces a depth-by-length heatmap of retrieval accuracy that visually exposes where a model's effective context degrades. The format was popularized as an informal evaluation by Greg Kamradt [@kamradt2023], and a closely related synthetic precursor is the "passkey retrieval" task used to probe context extension [@mohtashami2023]. NIAH measures verbatim retrieval/recall of an isolated fact rather than reasoning or aggregation over the context, so strong NIAH scores do not guarantee broader long-context competence. This limitation motivated harder, more diverse suites such as [[RULER]] and [[InfiniteBench]]. It contrasts with [[Long Range Arena]], which targets architectural long-range modeling rather than retrieval from natural-language context.

## Related
- [[RULER]]
- [[Long Range Arena]]
- [[LongBench]]
- [[InfiniteBench]]
- [[Context Window As Working Memory]]
- [[MOC - Evaluation and Benchmarks]]
