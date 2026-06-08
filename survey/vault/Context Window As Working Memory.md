---
title: Context Window As Working Memory
aliases: [Context Window, Working Memory, In-Context Memory]
tags: [llm-memory/context, concept]
status: draft
---

In a Transformer language model the context window is the finite span of tokens the model can attend to at once, and it functions as a form of volatile working memory: any information not encoded in the weights must be present in this window to influence the next prediction. Unlike parametric (long-term) memory stored in the model's weights, context memory is implicit and ephemeral, holding the current prompt, retrieved documents, and the running generation. Its effective capacity is bounded by the self-attention mechanism, whose compute and memory cost grow quadratically with sequence length [@vaswani2017], which historically capped windows at a few thousand tokens. Two practical limits shape it: a hard limit set by the trained maximum position, and a soft limit where models fail to use information in the middle of long contexts ("lost in the middle") [@liu2023lost]. Much of the work in this cluster aims to enlarge, cheapen, or better manage this working memory through positional encodings, efficient attention, KV-cache management, and context extension.

## Related
- [[Self-Attention And Quadratic Cost]]
- [[Lost In The Middle]]
- [[KV-Cache As Short-Term Memory]]
- [[Rotary Position Embedding]]
- [[MOC - Context Memory]]
