---
title: Differentiable Neural Computer
aliases: [DNC]
tags: [llm-memory/architecture, architecture]
status: draft
---

The Differentiable Neural Computer (DNC) extends the Neural Turing Machine with richer, more robust memory-management mechanisms, again pairing a neural controller with an external memory matrix accessed by differentiable read/write heads [@graves2016]. It adds three key innovations: a dynamic memory allocation scheme using a usage vector and a free list so the controller can find and reuse unused slots without interference; a temporal link matrix that records the order in which slots were written, enabling reading of memories in the sequence they were stored; and multiple read heads with content- plus allocation-based addressing. These let the DNC solve tasks requiring structured memory, such as answering questions over synthetic stories (bAbI), traversing graphs like the London Underground or family trees, and solving block-puzzle planning. Its limitations are practical: the architecture is complex and slow, training is brittle, and the dense memory addressing scales poorly, so DNCs were never adopted for large-scale language modeling. Conceptually, the DNC represents the high-water mark of explicit, fully-differentiable von-Neumann-style memory before the field shifted toward attention-based and retrieval-based memory.

## Related
- [[Neural Turing Machine]]
- [[Memory Networks]]
- [[Content-Based Addressing]]
- [[Parametric Vs Non-Parametric Memory]]
- [[MOC - Memory Architectures]]
