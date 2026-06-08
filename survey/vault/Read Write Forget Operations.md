---
title: Read Write Forget Operations
aliases: [Memory Operations, Read Write Forget, Memory CRUD, Add Update Delete Memory]
tags: [llm-memory/agent, concept]
status: draft
---

Agent memory systems can be decomposed into a small set of primitive operations over an external store, most usefully framed as **read**, **write**, and **forget** (with **update** often treated as forget-then-write) [@zhang2024memorysurvey]. **Reading** is the retrieval step: cueing the store with the current situation and surfacing relevant entries, typically via embedding similarity plus scoring by recency and importance [[Memory Retrieval Scoring (Recency Importance Relevance)]]. **Writing** is the encoding step: deciding *what* to store and in what form (raw episode, distilled fact, or executable skill), and *when* to write—on every observation, only on salient events, or after reflection. **Forgetting** is the deletion/decay step that keeps the store bounded and relevant: explicit eviction, time-based decay, importance thresholds, or consolidation that replaces many episodes with a summary. Most current systems implement read and write well but treat forgetting weakly—stores grow unbounded, stale facts persist, and there is no principled mechanism for selective deletion or conflict resolution. Framing memory as these operations exposes which capabilities a given system actually supports and is a common organizing axis in agent-memory surveys [@sumers2023; @wang2024survey]. The hard open problems are *write selectivity* (avoiding clutter) and *managed forgetting* (deleting without losing what later matters).

## Related
- [[Cognitive Memory Taxonomy For Agents]]
- [[Memory Retrieval Scoring (Recency Importance Relevance)]]
- [[Summarization As Long-Term Memory]]
- [[MemGPT And Virtual Context Management]]
- [[Catastrophic Forgetting]]
- [[MOC - Agent Memory]]
