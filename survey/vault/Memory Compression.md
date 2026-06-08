---
title: Memory Compression
aliases: [Memory Compression, Context Compression, Compressed Memory]
tags: [llm-memory/architecture, concept]
status: draft
---

Memory compression is the strategy of reducing the past context to a smaller representation so that long histories can be retained within a bounded memory budget, trading fidelity for capacity. Rather than caching every past activation, a compressing model maps many old states into fewer vectors or into a fixed-size state, accepting some information loss in exchange for the ability to reach much further back. Concrete instances span the recurrent-memory family: Compressive Transformers learn an explicit compression function (pooling or convolution) over aged-out activations and add an attention-reconstruction loss to preserve what attention uses [@rae2020]; the Recurrent Memory Transformer squeezes cross-segment context through a few learned memory tokens [@bulatov2022]; and Infini-attention compresses each segment into a fixed associative-memory matrix [@munkhdalai2024]. State-space and linear-attention models perform an implicit, continuous compression into a fixed hidden state [@gu2022]. The unifying limitation is that compression is lossy and capacity is finite: older or fine-grained details blur or get overwritten, so exact recall of arbitrary distant tokens is unreliable, and the model must learn *what* to keep. Compression is the central lever distinguishing recurrent-memory architectures from exact retrieval methods.

## Related
- [[Compressive Transformers]]
- [[Recurrent Memory Transformer]]
- [[Infini-Attention]]
- [[Linear Attention As Memory]]
- [[Mamba]]
- [[S4]]
- [[MOC - Memory Architectures]]
