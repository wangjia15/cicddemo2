---
title: Core Memory And Editable Persona
aliases: [Core Memory, Editable Memory Blocks, Persona Memory]
tags: [llm-memory/agent, concept]
status: draft
---

Core memory is a small, always-in-context region holding the most important persistent facts an agent should never page out: its own persona/instructions and key facts about the user. Introduced operationally by MemGPT, core memory is organized into editable **blocks** that the LLM can rewrite via function calls (e.g., `core_memory_append`, `core_memory_replace`) as it learns new stable information [@packer2023]. Because these blocks are pinned in the context window, they are read on every turn for free, giving the agent reliable, low-latency access to identity and user state without a retrieval call. Core memory implements a form of self-edited semantic memory: the agent consolidates durable facts out of the conversation and into a compact resident store. Its strength is guaranteed availability and cheap reads; its weaknesses are tight capacity (it competes for context budget), the risk of the model writing incorrect or contradictory facts, and the need for good policies about what is "core" versus archival.

## Related
- [[MemGPT And Virtual Context Management]]
- [[Semantic Memory In Agents]]
- [[Read Write Forget Operations]]
- [[Context Window As Working Memory]]
- [[MOC - Agent Memory]]
