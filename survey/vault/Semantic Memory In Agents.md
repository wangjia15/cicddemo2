---
title: Semantic Memory In Agents
aliases: [Semantic Memory, Knowledge Memory, Fact Memory]
tags: [llm-memory/agent, concept]
status: draft
---

Semantic memory holds an agent's distilled, time-independent knowledge: facts about the world, stable attributes of a user, learned generalizations, and relationships, as opposed to the raw events stored in episodic memory. In LLM agents it is realized as a maintained store of summarized facts, profile fields, or a knowledge graph that is updated as new experiences are abstracted. Generative Agents produce semantic content through **reflection**, where the agent periodically asks high-level questions over recent observations and writes back synthesized insights ("Klaus is passionate about research") that then participate in future retrieval [@park2023]. MemGPT-style systems maintain editable "core memory" blocks holding persistent facts about the persona and the user that are always kept in context [@packer2023]. Semantic memory enables consistency and efficient recall because a single distilled fact replaces many redundant episodes, but it risks staleness, over-generalization, and propagation of errors introduced during abstraction. The boundary with episodic memory is procedural: semantic facts are typically derived from episodes via summarization or reflection.

## Related
- [[Episodic Memory In Agents]]
- [[Reflection And Memory Consolidation]]
- [[Summarization As Long-Term Memory]]
- [[Core Memory And Editable Persona]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[MOC - Agent Memory]]
