---
title: MEMIT
aliases: [MEMIT, Mass-Editing Memory in a Transformer]
tags: [llm-memory/parametric-editing, method]
status: draft
---

MEMIT (Mass-Editing Memory In a Transformer) generalizes [[ROME]] from single edits to inserting thousands of factual associations at once [@meng2023]. Rather than updating a single layer, MEMIT spreads the update across a range of critical mid-layer MLPs identified by [[Causal Tracing]], solving a least-squares objective that simultaneously incorporates many new key-value memories while preserving existing ones. This makes it possible to update tens of thousands of facts in one pass with far better scaling than applying ROME repeatedly, which tends to accumulate damage. MEMIT became a standard strong baseline for batched [[Knowledge Editing]], evaluated on [[CounterFact]] and [[zsRE]] with metrics for efficacy, paraphrase generalization, and specificity. It shares ROME's reliance on the [[FFN As Key-Value Memory]] view and inherits debates about whether causal-tracing locations are the best edit sites.

## Related
- [[ROME]]
- [[Causal Tracing]]
- [[FFN As Key-Value Memory]]
- [[Knowledge Editing]]
- [[CounterFact]]
- [[zsRE]]
- [[MOC - Parametric Memory and Editing]]
