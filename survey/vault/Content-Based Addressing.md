---
title: Content-Based Addressing
aliases: [Content Addressing, Content-Addressable Memory, Associative Addressing]
tags: [llm-memory/architecture, concept]
status: draft
---

Content-based addressing is the mechanism by which a memory-augmented network locates information by *what it contains* rather than by a fixed numeric address, retrieving slots whose stored vectors are most similar to a query key. In differentiable memory models the controller emits a query, similarity (typically cosine or dot product) is computed against every memory slot, and a softmax turns these scores into a soft read weighting, so the read is a similarity-weighted average of slot contents [@graves2014]. This is the differentiable relaxation of an associative or content-addressable memory, and it is the same operation that underlies attention in modern Transformers, where queries match keys to pull out values [@sukhbaatar2015]. Neural Turing Machines combine content-based addressing with location-based addressing (shifting along rows) to support both associative recall and iterative, position-relative access. The principal limitation is cost and precision: scoring against every slot is linear in memory size, and as memories grow large, soft attention either becomes expensive or blurs across many similar slots, motivating approximate nearest-neighbor retrieval in later systems such as Memorizing Transformers.

## Related
- [[Neural Turing Machine]]
- [[Memory Networks]]
- [[End-to-End Memory Networks]]
- [[Differentiable Neural Computer]]
- [[Memorizing Transformers]]
- [[MOC - Memory Architectures]]
