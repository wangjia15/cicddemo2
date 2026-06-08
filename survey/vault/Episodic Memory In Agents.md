---
title: Episodic Memory In Agents
aliases: [Episodic Memory, Experience Memory, Memory Stream]
tags: [llm-memory/agent, concept]
status: draft
---

Episodic memory in an LLM agent stores specific, time-stamped experiences: observations, actions, dialogue turns, and their outcomes, recorded as discrete entries the agent can later recall. The canonical implementation is the **memory stream** of Generative Agents, an append-only list of natural-language observations each tagged with a creation timestamp and last-access time, retrieved on demand by relevance, recency, and importance [@park2023]. Episodic entries are typically embedded and stored in a vector index so that a current situation can cue the retrieval of analogous past episodes (e.g., "what happened last time I visited this shop"). Because episodic memory grows without bound, systems pair it with retrieval scoring, summarization, and reflection to keep recall tractable and to abstract recurring episodes into semantic knowledge. Episodic memory underpins continuity of identity and behaviour over long horizons, but it is sensitive to retrieval failures, embedding drift, and the cost of storing every event. It contrasts with semantic memory, which holds the distilled facts rather than the raw events.

## Related
- [[Generative Agents Memory Stream]]
- [[Memory Retrieval Scoring (Recency Importance Relevance)]]
- [[Semantic Memory In Agents]]
- [[Reflection And Memory Consolidation]]
- [[Cognitive Memory Taxonomy For Agents]]
- [[MOC - Agent Memory]]
