---
title: MOC - Parametric Memory and Editing
aliases: [Parametric Memory MOC, Knowledge Editing MOC, Parametric Editing MOC]
tags: [llm-memory/parametric-editing, moc]
status: draft
---

# Map of Content: Parametric Memory and Editing

This cluster covers **parametric memory** — the knowledge a language model stores implicitly in its weights — and the methods that **locate, edit, update, and forget** that knowledge. The organizing idea is that factual recall is partly localized in the Transformer's feed-forward layers, which lets us treat updating a fact as a targeted weight modification rather than full retraining.

## Framing
- [[Parametric Memory]] — knowledge baked into weights; compact and fluent but opaque and hard to update.
- [[Parametric Vs Non-Parametric Memory]] — the weights-vs-external-store distinction (shared with the retrieval cluster).
- [[FFN As Key-Value Memory]] — Geva et al.'s view of MLP sublayers as key-value memories, the mechanistic basis for editing.

## Locating Factual Knowledge
- [[Causal Tracing]] — activation patching to find where a fact is computed (mid-layer MLPs at the last subject token).
- [[Knowledge Neurons]] — attributing facts to individual FFN neurons.

## Editing Methods
### Locate-then-edit (closed-form weight updates)
- [[ROME]] — rank-one edit of one MLP layer for a single fact.
- [[MEMIT]] — mass-editing thousands of facts across critical layers.
### Meta-learning / hypernetwork editors
- [[MEND]] — gradient-decomposition hypernetwork for fast edits on large models.
- [[KnowledgeEditor]] — early learned editor predicting weight updates conditioned on the fact.
### Memory-based / semi-parametric
- [[SERAC]] — frozen base model plus external edit memory and a scope classifier.

## Updating, Forgetting, and Continual Learning
- [[Knowledge Editing]] — the overall task and its reliability/generalization/locality criteria.
- [[Knowledge Updating Vs Forgetting]] — two directions of the same control problem over weight memory.
- [[Catastrophic Forgetting]] — overwriting old knowledge when learning the new.
- [[Continual Learning]] — the stability-plasticity dilemma and lifelong updating.

## Evaluation (see also [[MOC - Evaluation and Benchmarks]])
- [[LAMA Probe]] — probing how much factual knowledge is stored parametrically.
- [[CounterFact]] — counterfactual editing benchmark with locality/generalization metrics.
- [[zsRE]] — QA-style editing benchmark.

## Suggested Reading Order
1. [[Parametric Memory]] → [[FFN As Key-Value Memory]]
2. [[Causal Tracing]] → [[Knowledge Neurons]]
3. [[ROME]] → [[MEMIT]] → [[MEND]] → [[KnowledgeEditor]] → [[SERAC]]
4. [[Knowledge Editing]] → [[Knowledge Updating Vs Forgetting]] → [[Catastrophic Forgetting]] → [[Continual Learning]]
5. [[LAMA Probe]] → [[CounterFact]] → [[zsRE]]
