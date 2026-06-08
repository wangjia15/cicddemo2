---
title: Longformer
aliases: [Longformer, Sliding Window Attention]
tags: [llm-memory/context, architecture]
status: draft
---

Longformer replaces full quadratic self-attention with a sparse pattern that scales linearly in sequence length, combining a sliding local window (each token attends to a fixed number of neighbors) with a small set of global tokens that attend to and are attended by all positions [@beltagy2020longformer]. Dilated windows can widen the local receptive field without extra cost, and the global tokens (e.g., the [CLS] token or question tokens) let task-relevant anchors integrate information across the whole sequence. This design lets the model process documents of thousands of tokens as working memory at manageable cost. Limitations are that local attention can miss long-range dependencies outside the window unless captured through global tokens or stacked layers, and the attention pattern must be chosen per task. Longformer is a foundational sparse-attention architecture alongside [[BigBird]].

## Related
- [[BigBird]]
- [[Self-Attention And Quadratic Cost]]
- [[FlashAttention]]
- [[Context Window As Working Memory]]
- [[MOC - Context Memory]]
