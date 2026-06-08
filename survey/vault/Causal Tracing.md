---
title: Causal Tracing
aliases: [Causal Tracing, Activation Patching for Facts, Locating Factual Knowledge]
tags: [llm-memory/parametric-editing, method]
status: draft
---

Causal tracing is a method introduced in the ROME paper for localizing where a factual association is computed inside a Transformer [@meng2022]. The model is run three times: a clean run on a factual prompt, a corrupted run where the subject tokens' embeddings are noised so the model fails, and restored runs where individual hidden states from the clean run are patched back into the corrupted run one at a time. States whose restoration most recovers the correct prediction are deemed causally important; this procedure revealed a decisive role for mid-layer MLP modules at the last subject token in factual recall. The technique is a form of activation patching applied specifically to factual prediction, and it motivated editing the identified MLP weights directly. Its conclusions have been debated: later work showed that where a fact can be edited does not always coincide with where causal tracing localizes it.

## Related
- [[ROME]]
- [[FFN As Key-Value Memory]]
- [[MEMIT]]
- [[Knowledge Editing]]
- [[MOC - Parametric Memory and Editing]]
