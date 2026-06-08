---
title: Generative Agents Memory Stream
aliases: [Generative Agents, Park et al. 2023, Smallville, Memory Stream]
tags: [llm-memory/agent, method]
status: draft
---

**Generative Agents** (Park et al.) populate an interactive sandbox ("Smallville") with believable simulacra of human behaviour, and their central contribution is a memory architecture with three components: a **memory stream**, **reflection**, and **planning** [@park2023]. The memory stream is a comprehensive, append-only record of the agent's experiences in natural language, each entry stamped with creation and last-access times. To act, the agent retrieves a relevant subset of memories using a scoring function that linearly combines **recency** (exponential decay since last access), **importance** (an LLM-assigned poignancy score), and **relevance** (embedding similarity to the current query) [[Memory Retrieval Scoring (Recency Importance Relevance)]]. Periodically the agent **reflects**, synthesizing higher-level inferences from recent memories and writing them back into the stream as new, retrievable observations, which lets behaviour build on abstractions rather than raw events. This pipeline produces emergent, coherent long-horizon behaviour (spreading party invitations, forming opinions) and is a foundational design for episodic agent memory. Limitations include high LLM cost from frequent retrieval/reflection calls, sensitivity of importance scoring to prompt design, and unbounded stream growth.

## Related
- [[Memory Retrieval Scoring (Recency Importance Relevance)]]
- [[Reflection And Memory Consolidation]]
- [[Episodic Memory In Agents]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[MOC - Agent Memory]]
