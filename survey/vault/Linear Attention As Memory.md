---
title: Linear Attention As Memory
aliases: [Linear Attention As Memory, Linear Attention, Fast Weights, Attention as RNN]
tags: [llm-memory/architecture, concept]
status: draft
---

Linear attention reframes attention as a recurrent memory: by replacing the softmax with a kernel feature map, the attention computation can be rewritten so that the model maintains a fixed-size matrix-valued state that is updated additively as each token arrives, rather than re-attending over all past keys and values [@katharopoulos2020]. This state is an outer-product associative memory (a "fast weight" matrix) into which key-value pairs are written and from which queries read, making inference linear in sequence length with constant memory, unlike the growing KV cache of standard attention. The same view explains why state-space models and gated linear-attention variants behave like compressed recurrent memories, and Infini-attention exploits exactly this to store a segment's keys and values into a fixed associative memory it later reads with current queries [@munkhdalai2024]. The core limitation is capacity and interference: a fixed-size state cannot losslessly store an unbounded history, so distinct memories collide and precise long-range recall degrades, which is why pure linear-attention models often trail full attention on retrieval-heavy tasks and motivate selective or hybrid designs.

## Related
- [[Infini-Attention]]
- [[Mamba]]
- [[S4]]
- [[Memory Compression]]
- [[KV-Cache As Short-Term Memory]]
- [[MOC - Memory Architectures]]
