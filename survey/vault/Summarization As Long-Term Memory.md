---
title: Summarization As Long-Term Memory
aliases: [Summarization Memory, Recursive Summarization, Compression Memory, Conversation Summary Memory]
tags: [llm-memory/agent, concept]
status: draft
---

A simple and widely deployed form of long-term memory is **summarization**: when a dialogue or task history exceeds the context window, the agent compresses older content into a shorter natural-language summary that stays resident while the verbatim text is dropped. **Recursive (rolling) summarization** maintains a running summary that is repeatedly updated as new turns arrive, an approach popularized in conversational frameworks and used in MemGPT to flush evicted messages into a compact recursive summary before paging them to external storage [@packer2023]. The technique was demonstrated at scale by recursively summarizing books for long-document abstraction [@wu2021recursively]. As a memory mechanism, summarization trades fidelity for capacity: it preserves the gist of a long history at constant context cost, and it doubles as a consolidation step that abstracts episodic detail into semantic content [[Semantic Memory In Agents]]. Its limitations are intrinsic and serious: summarization is lossy and irreversible, so details needed later may be discarded; errors compound across recursive passes; and the model may hallucinate or distort facts during compression. Consequently it is usually paired with a retrievable archival store so that specifics can still be recovered when the summary is insufficient.

## Related
- [[MemGPT And Virtual Context Management]]
- [[Reflection And Memory Consolidation]]
- [[Semantic Memory In Agents]]
- [[Read Write Forget Operations]]
- [[Compressive Transformers]]
- [[MOC - Agent Memory]]
