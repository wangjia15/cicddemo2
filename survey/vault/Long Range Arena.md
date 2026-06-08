---
title: Long Range Arena
aliases: [Long Range Arena, LRA]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

Long Range Arena (LRA) is a benchmark suite by Tay et al. for systematically evaluating how well models, especially efficient-Transformer variants, capture long-range dependencies [@tay2021]. It bundles six tasks with sequence lengths ranging from roughly 1K to 16K tokens, including ListOps (hierarchical reasoning), byte-level text classification and document matching, pixel-level image classification, and Pathfinder/Path-X (detecting whether two points in an image are connected). The tasks are deliberately diverse in modality and structure so that no single inductive bias dominates, and the suite reports both task accuracy and computational efficiency (speed and memory), enabling an accuracy-versus-cost comparison across architectures. LRA was influential in standardizing claims about "efficient attention" methods and exposing that many were not clearly better than vanilla attention on long-range reasoning. It targets architectural long-range modeling rather than the retrieval-style behavior probed by [[Needle In A Haystack]].

## Related
- [[Needle In A Haystack]]
- [[RULER]]
- [[Self-Attention And Quadratic Cost]]
- [[MOC - Evaluation and Benchmarks]]
