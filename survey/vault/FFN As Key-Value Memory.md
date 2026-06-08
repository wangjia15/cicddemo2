---
title: FFN As Key-Value Memory
aliases: [Feed-Forward as Memory, MLP Key-Value Memories, Transformer FFN Memories]
tags: [llm-memory/parametric-editing, concept]
status: draft
---

Geva et al. showed that the feed-forward (FFN/MLP) sublayers of a Transformer operate as key-value memories: the first linear layer's rows act as keys that detect input patterns, and the second layer's columns act as values that induce distributions over the output vocabulary [@geva2021]. Lower layers tend to capture shallow lexical and syntactic patterns, while upper layers store more semantic and factual associations, and the layer's output is a weighted sum of value vectors gated by key activations. A follow-up analysis framed FFN value vectors as promoting concepts directly in the vocabulary space, refining predictions across the network's depth [@geva2022]. This view underpins locate-and-edit methods: if a fact is stored as a specific key-value association in a particular MLP layer, then editing that fact reduces to modifying that layer's weights. ROME and MEMIT both build directly on this interpretation, treating mid-layer MLPs as the causal site of factual recall.

## Related
- [[Parametric Memory]]
- [[ROME]]
- [[MEMIT]]
- [[Knowledge Neurons]]
- [[Causal Tracing]]
- [[MOC - Parametric Memory and Editing]]
