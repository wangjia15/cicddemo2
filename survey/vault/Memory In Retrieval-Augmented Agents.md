---
title: Memory In Retrieval-Augmented Agents
aliases: [Retrieval-Augmented Agents, Agentic RAG Memory, Long-Term Memory Retrieval For Agents]
tags: [llm-memory/agent, concept]
status: draft
---

Most LLM-agent long-term memory is implemented as **retrieval augmentation over the agent's own history**: experiences, facts, and skills are embedded and written to a vector store, then retrieved by similarity at decision time and injected into the context window. This reuses the retrieve-then-generate machinery of [[Retrieval-Augmented Generation (RAG)]] but differs in a key way—the corpus is *self-authored and dynamic* (the agent writes its own memories) rather than a fixed external knowledge base, so the system must manage writing, scoring, and forgetting, not just reading [[Read Write Forget Operations]]. Generative Agents, MemGPT's archival memory, and Voyager's skill index are all instances: each embeds memory entries and performs nearest-neighbor retrieval, differing mainly in scoring (recency/importance/relevance) and in what is stored (episodes, facts, or executable skills) [@park2023; @packer2023; @wang2023voyager]. The same retrieval infrastructure—dense encoders, ANN indexes like FAISS/HNSW—applies [[Vector Databases And ANN Search]]. The strengths are unbounded capacity, updatability, and attributable recall; the weaknesses are inherited retrieval failure modes: embedding mismatch, top-k truncation that drops needed memories, retrieval of stale or contradictory entries, and the lost-in-the-middle problem once many memories are stuffed into context [[Retrieval Failure Modes And Hallucination]]. Retrieval is therefore necessary but not sufficient—agents pair it with summarization, reflection, and forgetting to keep the store useful.

## Related
- [[Retrieval-Augmented Generation (RAG)]]
- [[Vector Databases And ANN Search]]
- [[Memory Retrieval Scoring (Recency Importance Relevance)]]
- [[Retrieval Failure Modes And Hallucination]]
- [[Episodic Memory In Agents]]
- [[MOC - Agent Memory]]
