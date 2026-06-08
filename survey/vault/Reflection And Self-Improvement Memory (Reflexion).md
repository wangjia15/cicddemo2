---
title: Reflection And Self-Improvement Memory (Reflexion)
aliases: [Reflexion, Verbal Reinforcement, Self-Reflection Memory]
tags: [llm-memory/agent, method]
status: draft
---

**Reflexion** is a framework that improves an LLM agent across trials not by updating weights but by maintaining a memory of *verbal* self-feedback [@shinn2023]. After an episode, the agent receives a reward signal (often sparse: success/failure, a test result, or an LLM-evaluated critique), and a **self-reflection** module verbalizes *why* it failed and what to do differently; this natural-language reflection is appended to an episodic memory buffer. On the next attempt the stored reflections are placed in context, so the agent conditions on its own past lessons—"verbal reinforcement learning." This yields large gains on decision-making (ALFWorld), reasoning (HotPotQA), and code generation (HumanEval) without any gradient updates. Reflexion's memory is thus a self-improvement store of distilled lessons rather than raw events. Limitations: the buffer is bounded and must be summarized as it grows, the quality of improvement depends entirely on the reflection LLM's diagnostic accuracy, it needs a usable reward/evaluation signal, and bad reflections can mislead later attempts. It is closely related to but distinct from Generative-Agents reflection, which consolidates social/episodic insight rather than task error-correction.

## Related
- [[Reflection And Memory Consolidation]]
- [[Procedural And Skill Memory]]
- [[Voyager Skill Library]]
- [[Read Write Forget Operations]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[MOC - Agent Memory]]
