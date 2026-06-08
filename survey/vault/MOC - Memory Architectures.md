---
title: MOC - Memory Architectures
aliases: [Memory Architectures MOC, Memory-Augmented Architectures MOC]
tags: [llm-memory/architecture, moc]
status: draft
---

# Map of Content: Memory-Augmented Architectures

This cluster covers architectures that build memory **into the model itself** — through an explicit external memory module, through recurrence that carries state across a sequence, or through a fixed-size state that compresses history. It is the counterpart to the [[MOC - Retrieval Memory]] cluster (memory as an external, looked-up store) and to parametric-editing approaches (memory baked into weights). The organizing question here is: *where does long-range information live during computation, and how is it written, read, and bounded?*

## Framing
- [[Content-Based Addressing]] — retrieving by similarity to content; the read primitive shared by external-memory nets and attention.
- [[Segment-Level Recurrence]] — carrying state across fixed-length blocks; the backbone pattern of recurrent-memory Transformers.
- [[Memory Compression]] — trading fidelity for capacity to fit long history into a bounded budget.
- [[Linear Attention As Memory]] — viewing attention/SSMs as a fixed-size recurrent associative state.

## Early External-Memory Neural Networks
These pair a neural controller with an explicit, addressable memory accessed by (mostly) differentiable read/write operations.
- [[Memory Networks]] — controller plus addressable memory array; strong-supervision QA ancestor.
- [[End-to-End Memory Networks]] — soft-attention, weakly-supervised successor; direct ancestor of Transformer key-value attention.
- [[Neural Turing Machine]] — controller + memory matrix with content- and location-based addressing; learns algorithms.
- [[Differentiable Neural Computer]] — NTM with dynamic allocation and temporal links; high-water mark of von-Neumann-style differentiable memory.

## Recurrence / Segment-Level Memory in Transformers
These extend Transformers beyond a fixed window by carrying or retrieving past activations.
- [[Transformer-XL]] — caches previous-segment activations as extended context (with relative positions).
- [[Compressive Transformers]] — adds a compressed long-term memory beneath Transformer-XL's short-term cache.
- [[Recurrent Memory Transformer]] — passes a few learned memory tokens across segments; scales to 1M+ tokens.
- [[Memorizing Transformers]] — non-differentiable kNN lookup over a large bank of past key-value pairs.
- [[Infini-Attention]] — fixed-size compressive associative memory inside each attention layer for unbounded input.

## State-Space / Linear-Attention Alternatives (High Level)
These replace attention with a fixed-size recurrent state that *is* the memory.
- [[S4]] — structured linear state-space model; HiPPO-initialized state compresses long history.
- [[Mamba]] — selective (input-dependent) SSM; content-aware compression with fast streaming inference.

## Suggested Reading Order
1. [[Content-Based Addressing]] — the shared read primitive.
2. [[Memory Networks]] → [[End-to-End Memory Networks]] → [[Neural Turing Machine]] → [[Differentiable Neural Computer]].
3. [[Segment-Level Recurrence]] → [[Transformer-XL]] → [[Compressive Transformers]] → [[Recurrent Memory Transformer]].
4. [[Memorizing Transformers]] (retrieval bridge) → [[Infini-Attention]].
5. [[Linear Attention As Memory]] → [[S4]] → [[Mamba]].
6. Cross-cutting: [[Memory Compression]] and the contrast with [[MOC - Retrieval Memory]].

## See Also
- [[MOC - Retrieval Memory]] — external/non-parametric memory.
- [[KV-Cache As Short-Term Memory]] · [[Context Window As Working Memory]] · [[Parametric Vs Non-Parametric Memory]]
