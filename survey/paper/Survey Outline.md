# Survey Outline — Memory in Large Language Models

**Working title:** *A Survey of Memory in Large Language Models: Taxonomy, Mechanisms, and Evaluation*

This is the single source-of-truth outline. Each section lists its one-line abstract, the
wiki notes that feed it, and planned figures.

## Taxonomy (organizing axes)

We organize LLM memory along **where the information lives** and **how long it persists**:

- **Parametric memory** — knowledge baked into weights (pretraining; FFN key–value memories; editing).
- **Contextual / working memory** — the context window and KV-cache; long-context methods.
- **Non-parametric / external memory** — retrieval over text or vectors (RAG, RETRO, kNN-LM).
- **Architectural memory** — recurrence and learned memory slots (Transformer-XL, RMT, NTM/DNC).
- **Agent memory** — orchestrated read/write/forget over episodic, semantic, procedural stores.

Cross-cutting: **evaluation & benchmarks**, and **open challenges**.

## Section plan

1. **Introduction** — why memory matters for LLMs; scope; contributions. *Figure: LLM Memory Taxonomy (mindmap).*
2. **Background** — transformer, attention, context window as working memory; terminology. *Figure: Memory timeline.*
3. **A Taxonomy of LLM Memory** — the five categories above; definitions and axes. *Figure: taxonomy graph; comparison table.*
4. **Parametric Memory** — knowledge in weights; FFN as KV memory; knowledge editing (ROME, MEMIT, MEND); forgetting. Feeds: `MOC - Parametric Memory and Editing`.
5. **Contextual / Working Memory** — context window, positional encodings (RoPE, ALiBi), long-context attention (Longformer, BigBird, FlashAttention), KV-cache management (StreamingLLM, H2O, paged attention), context extension (PI, YaRN). Feeds: `MOC - Context Memory`. *Figure: KV-cache / attention-sink flowchart.*
6. **Non-parametric / External Memory** — RAG family (kNN-LM, REALM, RAG, RETRO, Atlas), dense retrieval, vector DBs/ANN. Feeds: `MOC - Retrieval Memory`. *Figure: RAG pipeline flowchart.*
7. **Architectural Memory** — NTM/DNC, Memory Networks, Transformer-XL, Compressive Transformers, RMT, Memorizing Transformers, Infini-attention; SSMs (Mamba). Feeds: `MOC - Memory Architectures`. *Figure: segment-recurrence diagram.*
8. **Agent Memory Systems** — cognitive memory types; MemGPT, generative agents, Reflexion, Voyager; read/write/forget operations. Feeds: `MOC - Agent Memory`. *Figure: agent memory architecture; sequence diagram.*
9. **Evaluation & Benchmarks** — long-context (LRA, needle-in-a-haystack, RULER, LongBench, InfiniteBench), factual probing (LAMA), editing (CounterFact, zsRE). Feeds: `MOC - Evaluation and Benchmarks`. *Table: benchmarks.*
10. **Open Challenges & Future Directions** — unbounded/lifelong memory, consolidation, forgetting, faithfulness/attribution, evaluation gaps, efficiency.
11. **Conclusion.**

## Status tracker
- [x] Wiki notes — 84 atomic notes + 6 MOCs in `survey/vault/`
- [x] references.bib — 64 verified entries; keys match all `[@cite]` usages
- [x] Sections 1–11 drafts — in `survey/paper/sections/`
- [x] Mermaid figures — 6 figures, validated via mermaid-cli
- [x] Citation audit — 0 missing, 0 orphan keys
- [x] Assemble `paper.md` — ~14,900 words with embedded figures + reference list
