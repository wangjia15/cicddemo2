---
title: Compressive Transformers
aliases: [Compressive Transformer]
tags: [llm-memory/architecture, architecture]
status: draft
---

The Compressive Transformer augments Transformer-XL's segment-level recurrence with a second, longer-term memory that stores compressed representations of the distant past instead of discarding it [@rae2020]. It maintains two memories: a short-term memory of recent activations (as in Transformer-XL) and a compressed memory; when activations age out of the short-term memory they are passed through a learned compression function (e.g. convolution or pooling) that maps several old states into fewer "compressed" memory vectors. The model attends over both memories, so it can reach further back in the sequence at a sub-linear growth in stored state. The paper also introduced an attention-reconstruction auxiliary loss to train the compression to preserve information that attention actually uses, and released the PG-19 long-range language-modeling benchmark. Limitations include the added complexity of the compression step, lossy compression that can discard useful detail, and a memory that, while longer, is still finite and fades with age. It illustrates the broader theme of trading fidelity for capacity in recurrent Transformer memory.

## Related
- [[Transformer-XL]]
- [[Recurrent Memory Transformer]]
- [[Infini-Attention]]
- [[Memory Compression]]
- [[MOC - Memory Architectures]]
