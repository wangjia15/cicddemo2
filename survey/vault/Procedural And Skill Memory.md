---
title: Procedural And Skill Memory
aliases: [Procedural Memory, Skill Memory, Skill Library]
tags: [llm-memory/agent, concept]
status: draft
---

Procedural memory stores *how to act*: reusable skills, action policies, and executable procedures the agent can invoke rather than re-derive each time. In LLM agents it is most cleanly realized by **Voyager**, which builds an ever-growing **skill library** of executable code: each successfully verified behaviour is stored as a function, indexed by an embedding of its description, and retrieved and composed to solve harder tasks in Minecraft [@wang2023voyager]. This makes procedural memory compositional and lifelong: complex skills are built from simpler stored ones, and the library only grows. More broadly, procedural memory can take the form of tool-use routines, learned prompts, or cached reasoning chains. Compared with episodic and semantic memory, procedural memory is action-oriented and is validated by execution success rather than by recall accuracy, which gives it a natural correctness signal (the code runs or it does not). Limitations include skill brittleness under environment shifts, retrieval of an inappropriate skill, and unbounded growth of the library without pruning or abstraction.

## Related
- [[Voyager Skill Library]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[Reflection And Self-Improvement Memory (Reflexion)]]
- [[Read Write Forget Operations]]
- [[MOC - Agent Memory]]
