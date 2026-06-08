## 1. Introduction

Large language models (LLMs) built on the Transformer architecture [@vaswani2017] have become
general-purpose engines for language understanding and generation. As they are deployed in
longer conversations, document-scale reasoning, and multi-step autonomous tasks, a single
faculty increasingly governs what they can and cannot do: **memory**. Whether a model can
recall a fact stated thousands of tokens ago, incorporate knowledge that postdates its
training, maintain a consistent persona across a week-long interaction, or accumulate skills
over a long-horizon task are all, at root, questions about how information is stored, retained,
and retrieved.

The difficulty is that "memory" in LLMs is not one mechanism but several, operating at
different locations and timescales. Knowledge acquired during pretraining is compressed into
the model's weights and is, by default, fixed and opaque [@geva2021]. The context window holds
the immediate inputs as a form of volatile working memory, but at a cost that grows
quadratically with length and with no guarantee that distant content is actually used
[@liu2023lost]. External corpora can be consulted at inference time through retrieval, decoupling
knowledge from parameters [@lewis2020]. Specialized architectures add recurrent state or
learnable memory slots that persist across segments [@dai2019]. And LLM-based agents wrap the
model in explicit read/write/forget machinery over episodic, semantic, and procedural stores
[@packer2023; @park2023]. These mechanisms are studied in largely separate literatures, with
different vocabularies and evaluation practices, which makes it hard to see the field as a
whole.

This survey provides that unifying view. We make three contributions:

1. **A taxonomy.** We organize LLM memory by *where* information resides and *how long* it
   persists, yielding five categories — parametric, contextual/working, non-parametric/external,
   architectural, and agent memory (Figure: LLM Memory Taxonomy). The taxonomy situates methods
   that are usually discussed in isolation within a single frame and exposes their trade-offs.
2. **A mechanism-level synthesis.** For each category we explain the core mechanism, survey
   representative systems from foundational work to recent advances, and state the limitations
   that motivate the next category. We connect threads that recur across categories — content-based
   addressing, compression-versus-fidelity, and updatability — rather than treating each system
   as a point solution.
3. **An account of evaluation.** We survey how memory is measured, from efficiency benchmarks
   and long-context stress tests to factual probing and knowledge-editing suites, and we
   emphasize the persistent gap between a model's *nominal* memory capacity (e.g., a context
   window of a given size) and its *effective* capacity (what it can actually use reliably).

**Scope.** We focus on memory in and around Transformer-based LLMs. We include the
memory-augmented neural networks that precede them, because they introduced ideas — external
addressable memory, differentiable read/write — that reappear throughout the modern literature.
We treat efficiency and serving systems (e.g., KV-cache management) where they bear directly on
memory behavior, but we do not attempt a complete survey of efficient inference. We likewise
touch state-space models as an architectural memory alternative without surveying sequence
modeling in full.

**Organization.** Section 2 reviews background on the Transformer, the context window, and our
working definition of memory. Section 3 presents the taxonomy. Sections 4–8 treat the five
categories in turn: parametric memory and knowledge editing (Section 4), contextual and working
memory (Section 5), non-parametric and external memory (Section 6), architectural memory
(Section 7), and agent memory systems (Section 8). Section 9 surveys evaluation and benchmarks.
Section 10 discusses open challenges and future directions, and Section 11 concludes.
