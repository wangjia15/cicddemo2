---
title: KnowledgeEditor
aliases: [KnowledgeEditor, KE, Hypernetwork Knowledge Editor, Editing Factual Knowledge in Language Models]
tags: [llm-memory/parametric-editing, method]
status: draft
---

KnowledgeEditor is a hypernetwork-based editor from De Cao et al. that learns to modify a model's stored factual knowledge by predicting weight updates conditioned on the fact to be changed [@decao2021]. It frames editing as a constrained optimization: change the prediction for a target input while keeping the model's behavior on other inputs as unchanged as possible, and trains a separate network (the editor) to output the required parameter shift. Because the editor is learned, edits are fast at inference and do not require gradient steps on the base model itself. The paper established the now-standard evaluation axes of edit success, generalization to semantically equivalent inputs, and retention of unrelated predictions, and it influenced the gradient-decomposition design of [[MEND]]. It is one of the earliest learned hypernetwork editors for large language models.

## Related
- [[MEND]]
- [[SERAC]]
- [[Knowledge Editing]]
- [[zsRE]]
- [[MOC - Parametric Memory and Editing]]
