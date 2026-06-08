---
title: Knowledge Updating Vs Forgetting
aliases: [Knowledge Updating, Updating vs Forgetting, Memory Updating, Knowledge Staleness]
tags: [llm-memory/parametric-editing, concept]
status: draft
---

Keeping a model's parametric memory current requires both adding or revising facts (updating) and removing or suppressing outdated or unwanted ones (forgetting), and the difficulty is doing either surgically without collateral damage. Updating is the goal of [[Knowledge Editing]]: insert a new fact, change an answer, or correct a stale association while preserving unrelated knowledge, measured by reliability, generalization, and locality. Intentional, targeted forgetting — erasing a specific fact, capability, or memorized private text — is studied as machine unlearning, where the aim is to make the model behave as if it had never seen the target data while retaining everything else. The unwanted counterpart is [[Catastrophic Forgetting]], where learning the new silently overwrites the old; this stability-plasticity tension is the core problem of [[Continual Learning]]. Sequential editing makes the tension acute: applying many edits in turn tends to accumulate interference and drift, degrading both edited and unrelated facts, which is why batched ([[MEMIT]]) and external-memory ([[SERAC]]) approaches are attractive. In short, updating and forgetting are two directions of the same control problem over distributed weight memory.

## Related
- [[Knowledge Editing]]
- [[Catastrophic Forgetting]]
- [[Continual Learning]]
- [[MEMIT]]
- [[SERAC]]
- [[Parametric Memory]]
- [[MOC - Parametric Memory and Editing]]
