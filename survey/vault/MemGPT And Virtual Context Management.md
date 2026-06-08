---
title: MemGPT And Virtual Context Management
aliases: [MemGPT, Virtual Context, OS-Style Memory Management, Letta]
tags: [llm-memory/agent, method]
status: draft
---

**MemGPT** treats the LLM's limited context window like the physical RAM of an operating system and builds a virtual-memory hierarchy on top of it, so an agent can appear to have unbounded memory [@packer2023]. The fixed context (**main context**) is analogous to RAM; an external store (**external context**: archival vector memory and a recall/message store) is analogous to disk. The LLM itself acts as the "processor": through function calls it **pages** information between tiers, deciding when to evict older messages to external storage and when to fetch relevant entries back into context. A self-directed control loop, driven by interrupts and memory-pressure warnings, lets the model issue read/write operations to its own memory, edit always-resident **core memory** blocks, and search archival memory. The result is effectively unbounded conversational and document memory without retraining, demonstrated on long multi-session dialogue and document QA. The idea—an LLM managing its own tiered memory via tool calls—has been influential (continued as the Letta project). Limitations include reliance on the model reliably emitting correct memory-management calls, latency and cost from extra LLM turns, and failures when the controller pages out information it later needs.

## Related
- [[Context Window As Working Memory]]
- [[Core Memory And Editable Persona]]
- [[Read Write Forget Operations]]
- [[Summarization As Long-Term Memory]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[MOC - Agent Memory]]
