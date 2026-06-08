---
title: Cognitive Memory Taxonomy For Agents
aliases: [Memory Taxonomy, Short-Term vs Long-Term Memory, Episodic Semantic Procedural Memory]
tags: [llm-memory/agent, concept]
status: draft
---

LLM-agent memory designs frequently borrow the cognitive-science distinction between **short-term/working memory** and **long-term memory**, mapping each onto concrete engineering substrates. Short-term (working) memory is the volatile, capacity-bounded buffer the agent reasons over right now, almost always realized as the model's context window plus a scratchpad of recent observations and intermediate thoughts [[Context Window As Working Memory]]. Long-term memory is an external, persistent store the agent reads from and writes to across episodes, typically a vector database, key-value store, or text log. Long-term memory is further subdivided, following Tulving's psychology, into **episodic** memory (specific time-stamped experiences and events), **semantic** memory (distilled facts and general knowledge about the world or user), and **procedural** memory (skills, action policies, and reusable code) [@tulving1985]. Surveys of agent cognition use this taxonomy to organize otherwise disparate systems and to expose missing capabilities such as forgetting and consolidation [@sumers2023; @zhang2024memorysurvey]. The taxonomy is a useful scaffold rather than a strict ontology: real systems blur the boundaries, and the mapping from human memory types to data structures is loose. Still, it clarifies why, for example, Voyager's skill library is "procedural" while Generative Agents' memory stream is largely "episodic."

## Related
- [[Context Window As Working Memory]]
- [[Episodic Memory In Agents]]
- [[Semantic Memory In Agents]]
- [[Procedural And Skill Memory]]
- [[Cognitive Architectures For Language Agents (CoALA)]]
- [[Read Write Forget Operations]]
- [[MOC - Agent Memory]]
