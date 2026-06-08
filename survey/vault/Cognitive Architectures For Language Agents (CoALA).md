---
title: Cognitive Architectures For Language Agents (CoALA)
aliases: [CoALA, Cognitive Architectures For Language Agents, Sumers et al. 2023]
tags: [llm-memory/agent, concept]
status: draft
---

**CoALA** is a conceptual framework that organizes language-agent designs by drawing on classic cognitive architectures (e.g., Soar, ACT-R), and it gives the agent-memory literature a shared vocabulary [@sumers2023]. It proposes that an agent be analyzed along three axes: its **memory components**, its **action space**, and its **decision-making procedure**. For memory, CoALA distinguishes **working memory** (the transient context the agent reasons over now) from three long-term stores—**episodic** (past experiences), **semantic** (facts and world knowledge), and **procedural** (skills, including the LLM weights themselves and agent code)—mirroring the cognitive taxonomy used throughout this cluster [[Cognitive Memory Taxonomy For Agents]]. The action space is split into **internal actions** (reasoning, retrieval, and learning that read/write memory) and **external actions** (grounding in an environment), which cleanly situates memory read/write as first-class agent actions [[Read Write Forget Operations]]. CoALA is a survey/position framework rather than a system: its value is taxonomic clarity, retrospective organization of prior work (MemGPT, Generative Agents, Voyager, Reflexion), and a forward-looking agenda. Its limitation is that the mapping from human cognitive constructs to LLM substrates is loose and prescriptive rather than empirically validated, so the framework guides design more than it predicts behaviour.

## Related
- [[Cognitive Memory Taxonomy For Agents]]
- [[Read Write Forget Operations]]
- [[Episodic Memory In Agents]]
- [[Semantic Memory In Agents]]
- [[Procedural And Skill Memory]]
- [[MOC - Agent Memory]]
