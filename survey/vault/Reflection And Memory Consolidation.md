---
title: Reflection And Memory Consolidation
aliases: [Reflection, Memory Consolidation, Insight Synthesis]
tags: [llm-memory/agent, concept]
status: draft
---

Reflection is the process by which an agent periodically reviews accumulated low-level memories and synthesizes higher-level insights that are written back into long-term store, consolidating raw episodes into reusable semantic knowledge. In Generative Agents, reflection triggers when the summed importance of recent observations crosses a threshold; the agent then poses salient questions over those memories and uses the LLM to generate abstract inferences (e.g., relationships, preferences), each stored as a new memory node linked to its evidence [@park2023]. This is functionally analogous to human memory consolidation: it compresses many episodic traces into fewer, more general, more retrievable statements, and it lets later reasoning build on abstractions instead of scanning raw events. Reflection improves coherence and long-horizon behaviour and reduces retrieval load, but it is costly (extra LLM calls), can compound errors if a faulty inference is stored as fact, and its trigger and depth are sensitive hyperparameters. It is distinct from Reflexion's verbal self-critique, though both turn experience into stored guidance.

## Related
- [[Generative Agents Memory Stream]]
- [[Semantic Memory In Agents]]
- [[Summarization As Long-Term Memory]]
- [[Reflection And Self-Improvement Memory (Reflexion)]]
- [[MOC - Agent Memory]]
