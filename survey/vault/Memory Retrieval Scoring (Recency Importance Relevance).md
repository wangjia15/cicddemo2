---
title: Memory Retrieval Scoring (Recency Importance Relevance)
aliases: [Retrieval Scoring, Recency Importance Relevance, RIR Scoring]
tags: [llm-memory/agent, concept]
status: draft
---

When an agent's long-term store grows beyond what fits in context, it must *select* which memories to surface, and a influential heuristic comes from Generative Agents: score each candidate memory by a weighted sum of three signals and return the top-k [@park2023]. **Recency** rewards recently accessed memories via exponential time decay (often with a per-step decay factor), modelling forgetting curves. **Importance** is an absolute salience score the LLM assigns when the memory is created (e.g., rating poignancy 1–10), letting mundane and pivotal events be weighted differently. **Relevance** is the cosine similarity between the query embedding and the memory embedding, capturing topical match to the current situation. The three components are normalized to [0,1] and combined (in the original work, with equal weights) into a final retrieval score. This scoring scheme is widely reused because it cheaply approximates human-like recall and is tunable, but it has limits: weights are hand-set and brittle, importance scoring adds LLM cost and noise, and pure top-k retrieval can miss memories that matter only in combination or that require multi-hop reasoning.

## Related
- [[Generative Agents Memory Stream]]
- [[Episodic Memory In Agents]]
- [[Memory In Retrieval-Augmented Agents]]
- [[Read Write Forget Operations]]
- [[MOC - Agent Memory]]
