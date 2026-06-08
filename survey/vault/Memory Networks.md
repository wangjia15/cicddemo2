---
title: Memory Networks
aliases: [MemNN, Memory Network]
tags: [llm-memory/architecture, architecture]
status: draft
---

Memory Networks are a class of neural models that augment a network with a large, addressable external memory array that can be read from and written to, designed so that long-term facts can be stored and later retrieved for reasoning [@weston2015]. The original formulation has four learned components: an input feature map (I), a generalization module (G) that updates memory slots, an output module (O) that scores memory slots against a query to select supporting facts, and a response module (R) that converts the retrieved memories into an answer. It was demonstrated on question answering over a set of supporting sentences, where the model must chain several stored facts to produce an answer. A key limitation of this first version is that it requires strong supervision: the correct supporting memories at each reasoning step must be labeled during training, because the hard argmax memory selection is not differentiable end-to-end. This non-differentiable addressing motivated the soft-attention successor, End-to-End Memory Networks. The design established the influential template of separating a controller from an explicit, content-addressable memory.

## Related
- [[End-to-End Memory Networks]]
- [[Neural Turing Machine]]
- [[Content-Based Addressing]]
- [[Parametric Vs Non-Parametric Memory]]
- [[MOC - Memory Architectures]]
