---
title: End-to-End Memory Networks
aliases: [MemN2N, End-To-End Memory Network]
tags: [llm-memory/architecture, architecture]
status: draft
---

End-to-End Memory Networks (MemN2N) make the original Memory Networks differentiable by replacing the hard, supervised memory selection with a soft attention read over all memory slots [@sukhbaatar2015]. Each input fact is embedded into both a "key" memory and a "value" memory; a query is matched against the keys via a softmax to produce attention weights, and the weighted sum of values is returned and added back to the query. Stacking several such read "hops" lets the model perform multi-step reasoning, attending to different facts at each hop, and the whole network is trained with only the final answer as supervision (weak supervision). It was applied to synthetic question answering (bAbI) and to language modeling, where the memory acts over recent words. Because attention is computed over every stored slot at once, the memory is fixed-size per example and the read cost grows linearly with the number of slots, limiting scalability to very large memories. MemN2N is a direct conceptual ancestor of the key-value attention used throughout modern Transformers.

## Related
- [[Memory Networks]]
- [[Content-Based Addressing]]
- [[Memorizing Transformers]]
- [[Context Window As Working Memory]]
- [[MOC - Memory Architectures]]
