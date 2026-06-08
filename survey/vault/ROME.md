---
title: ROME
aliases: [ROME, Rank-One Model Editing, Locating and Editing Factual Associations]
tags: [llm-memory/parametric-editing, method]
status: draft
---

ROME (Rank-One Model Editing) is a method for editing a single factual association in a GPT-style model by directly modifying the weights of one mid-layer MLP [@meng2022]. Using [[Causal Tracing]], the authors localize factual recall to mid-layer feed-forward modules at the last subject token, then treat that MLP's second linear layer as a linear associative memory mapping a key (the subject representation) to a value (a vector that elicits the target object). The edit is a rank-one update to the weight matrix, computed in closed form to insert a new key-value pair while minimally disturbing existing associations. ROME edits one fact at a time and substantially improves generalization to paraphrases compared with naive fine-tuning, while keeping unrelated predictions stable. Its main limitation is scale: it does not batch many edits at once, which motivated [[MEMIT]].

## Related
- [[MEMIT]]
- [[Causal Tracing]]
- [[FFN As Key-Value Memory]]
- [[Knowledge Editing]]
- [[CounterFact]]
- [[MOC - Parametric Memory and Editing]]
