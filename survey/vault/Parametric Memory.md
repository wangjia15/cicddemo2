---
title: Parametric Memory
aliases: [Weight Memory, Implicit Knowledge, Parametric Knowledge]
tags: [llm-memory/parametric-editing, concept]
status: draft
---

Parametric memory is the knowledge a language model stores implicitly in its weights, acquired during pretraining and retrieved through a forward pass rather than by reading an external store. It is compact, fast, and supports fluent generalization, but is opaque, expensive to update, and prone to staleness and hallucination. Empirically, much factual recall localizes to the feed-forward (MLP) sublayers of the Transformer, which behave like key-value memories that emit distributions over the vocabulary [@geva2021]. Probing studies such as the LAMA benchmark showed that pretrained models already encode a surprising amount of relational knowledge accessible through cloze queries [@petroni2019]. Because this memory lives in distributed weights, updating a single fact ideally without disturbing others is the central problem of [[Knowledge Editing]]. Parametric memory contrasts with non-parametric memory held in retrievable external stores.

## Related
- [[FFN As Key-Value Memory]]
- [[Knowledge Editing]]
- [[Knowledge Neurons]]
- [[LAMA Probe]]
- [[Catastrophic Forgetting]]
- [[MOC - Parametric Memory and Editing]]
