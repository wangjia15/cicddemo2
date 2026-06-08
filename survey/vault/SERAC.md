---
title: SERAC
aliases: [SERAC, Semi-Parametric Editing with a Retrieval-Augmented Counterfactual Model, Memory-Based Model Editing]
tags: [llm-memory/parametric-editing, method]
status: draft
---

SERAC is a memory-based model-editing method that keeps the base model's weights frozen and instead stores edits in an explicit external memory [@mitchell2022serac]. At inference a learned scope classifier decides whether an input falls under any stored edit; if so, a separate small counterfactual model produces the edited prediction, otherwise the original model answers normally. This semi-parametric design avoids the risk of locate-and-edit weight surgery damaging unrelated knowledge, making edits easy to add, revise, or roll back, and it handles sequences of many edits gracefully. SERAC introduced harder evaluation settings emphasizing that edits should generalize and not leak into out-of-scope inputs, and it is a common baseline contrasting with weight-modifying editors like [[ROME]] and [[MEND]]. Conceptually it blurs the line between [[Knowledge Editing]] and retrieval-based memory.

## Related
- [[MEND]]
- [[KnowledgeEditor]]
- [[ROME]]
- [[Knowledge Editing]]
- [[MOC - Parametric Memory and Editing]]
