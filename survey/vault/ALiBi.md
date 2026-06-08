---
title: ALiBi
aliases: [Attention with Linear Biases, ALiBi]
tags: [llm-memory/context, method]
status: draft
---

ALiBi (Attention with Linear Biases) removes learned positional embeddings entirely and instead adds a static, negative bias to attention scores that grows linearly with the distance between query and key, with a different fixed slope per attention head [@press2021alibi]. This penalizes attending to distant tokens in a simple, parameter-free way and biases each head toward a characteristic context range. Its headline property is length extrapolation: a model trained on short sequences can be evaluated on much longer ones with little degradation, treating the longer span as usable working memory without retraining. ALiBi is cheap to implement and adds no parameters, but its built-in recency bias can hurt tasks that need to retrieve information from far back in the context, and it is less expressive than rotary schemes for some relative-position patterns. It is often compared directly with [[Rotary Position Embedding]] as an alternative route to length generalization.

## Related
- [[Rotary Position Embedding]]
- [[Length Generalization And Extrapolation]]
- [[Position Interpolation]]
- [[Self-Attention And Quadratic Cost]]
- [[MOC - Context Memory]]
