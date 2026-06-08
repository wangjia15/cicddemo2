---
title: CounterFact
aliases: [CounterFact, COUNTERFACT]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

CounterFact is a benchmark introduced with [[ROME]] for evaluating factual [[Knowledge Editing]], built specifically to distinguish genuine knowledge change from superficial parroting [@meng2022]. Each record pairs a true fact with a counterfactual target and provides paraphrase prompts (to test generalization), neighborhood prompts about related but distinct subjects (to test locality/specificity), and generation prompts (to test that edits propagate into free-form text). Its metrics include efficacy (the edited fact is now predicted), paraphrase/generalization score, specificity/neighborhood score (unrelated facts unchanged), plus fluency and consistency measures of generated text. Because counterfactual targets are usually false in the world, an edit's success cannot be explained by the fact already being known, making CounterFact a stringent test. It and [[zsRE]] are the two standard editing benchmarks used by [[ROME]], [[MEMIT]], and hypernetwork editors.

## Related
- [[zsRE]]
- [[ROME]]
- [[MEMIT]]
- [[Knowledge Editing]]
- [[MOC - Evaluation and Benchmarks]]
