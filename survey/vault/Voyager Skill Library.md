---
title: Voyager Skill Library
aliases: [Voyager, Skill Library, Lifelong Skill Memory]
tags: [llm-memory/agent, method]
status: draft
---

**Voyager** is an LLM-powered embodied agent that plays Minecraft via lifelong learning, and its memory contribution is a **skill library** of executable code that functions as procedural long-term memory [@wang2023voyager]. The agent has three coupled components: an automatic curriculum that proposes progressively harder goals, an iterative prompting loop that writes JavaScript control code refined by environment-execution feedback and self-verification, and the skill library itself. When a program completes a task and passes verification, it is stored as a reusable skill, indexed by an embedding of a GPT-generated description; for new tasks, relevant skills are retrieved and composed, so capabilities compound over time without forgetting. Because skills are code, retrieval returns directly executable behaviour, and verification gives a hard correctness signal that gates what enters memory. Voyager substantially outperforms prior agents on exploration breadth and tech-tree progress and shows strong transfer to new worlds. Limitations include dependence on a code-capable backbone, brittleness of skills to environment changes, retrieval of inappropriate skills, and unbounded library growth without consolidation. It is the cleanest example of procedural/skill memory in LLM agents.

## Related
- [[Procedural And Skill Memory]]
- [[Reflection And Self-Improvement Memory (Reflexion)]]
- [[Memory In Retrieval-Augmented Agents]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[MOC - Agent Memory]]
