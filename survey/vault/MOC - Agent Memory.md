---
title: MOC - Agent Memory
aliases: [Agent Memory MOC, LLM-Agent Memory Systems MOC]
tags: [llm-memory/agent, moc]
status: draft
---

# Map of Content: LLM-Agent Memory Systems

This cluster covers **memory in LLM-based autonomous agents**: how an agent that reasons in a bounded context window acquires persistent memory across turns, episodes, and tasks. The unifying idea is to treat the context window as volatile *working memory* and to build *long-term memory* as an external store the agent reads from, writes to, and forgets—often structured along a cognitive taxonomy (episodic, semantic, procedural). Each note explains the idea, mechanism, and limitations.

## Framing And Taxonomy
- [[Cognitive Memory Taxonomy For Agents]] — short-term/working vs long-term; episodic, semantic, procedural.
- [[Cognitive Architectures For Language Agents (CoALA)]] — the cognitive-architecture framework organizing the whole space.
- [[Read Write Forget Operations]] — the primitive operations any memory system must implement.

## Memory Types
- [[Context Window As Working Memory]] — the volatile, in-context short-term store.
- [[Episodic Memory In Agents]] — time-stamped experiences and events.
- [[Semantic Memory In Agents]] — distilled facts, world and user knowledge.
- [[Procedural And Skill Memory]] — reusable skills, policies, and executable routines.

## OS-Style Memory Management
- [[MemGPT And Virtual Context Management]] — the LLM as an OS paging between RAM-like context and disk-like external store.
- [[Core Memory And Editable Persona]] — small, always-resident, self-edited memory blocks.

## Generative Agents And Retrieval Scoring
- [[Generative Agents Memory Stream]] — Park et al.'s memory stream + reflection + retrieval.
- [[Memory Retrieval Scoring (Recency Importance Relevance)]] — the recency/importance/relevance read heuristic.
- [[Reflection And Memory Consolidation]] — synthesizing higher-level insight from raw episodes.

## Self-Improvement And Skill Memory
- [[Reflection And Self-Improvement Memory (Reflexion)]] — verbal self-feedback stored as memory.
- [[Voyager Skill Library]] — a growing library of verified, executable skills as procedural memory.

## Retrieval And Compression Substrates
- [[Memory In Retrieval-Augmented Agents]] — retrieval over the agent's self-authored memory store.
- [[Summarization As Long-Term Memory]] — compression/recursive summarization as memory.

## Suggested Reading Order
1. [[Cognitive Memory Taxonomy For Agents]] → [[Cognitive Architectures For Language Agents (CoALA)]] → [[Read Write Forget Operations]]
2. [[Context Window As Working Memory]] → [[MemGPT And Virtual Context Management]] → [[Core Memory And Editable Persona]]
3. [[Generative Agents Memory Stream]] → [[Memory Retrieval Scoring (Recency Importance Relevance)]] → [[Reflection And Memory Consolidation]]
4. [[Reflexion|Reflection And Self-Improvement Memory (Reflexion)]] → [[Voyager Skill Library]] → [[Procedural And Skill Memory]]
5. [[Memory In Retrieval-Augmented Agents]] → [[Summarization As Long-Term Memory]]

## See Also
- [[MOC - Retrieval Memory]] — external/non-parametric memory and RAG machinery.
- [[MOC - Context Memory]] — context windows, efficient attention, KV-cache.
