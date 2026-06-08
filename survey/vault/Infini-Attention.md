---
title: Infini-Attention
aliases: [Infini-attention, Infini Transformer, Infinite Attention]
tags: [llm-memory/architecture, architecture]
status: draft
---

Infini-attention enables Transformers to process unbounded-length inputs with bounded memory by combining local self-attention with a compressive long-term memory inside each attention layer [@munkhdalai2024]. Within a segment the model performs ordinary masked attention; in parallel it maintains a fixed-size associative memory matrix into which it writes the segment's keys and values (using a linear-attention / fast-weight update), and it reads from this memory using the current queries. The local attention output and the memory-retrieval output are blended by a learned gating scalar, so each block sees both fine-grained recent context and a compressed summary of all earlier segments. Because the long-term memory has a fixed size regardless of sequence length, compute and memory stay constant per segment, allowing streaming over very long inputs (reported to millions of tokens) while reusing a standard Transformer backbone. The main limitation is that the long-term memory is a fixed-capacity, lossy compression: as more is written it must overwrite or blur older content, so precise recall of arbitrary distant details degrades, and the gating must learn what to keep. It sits at the intersection of recurrent memory, compression, and linear-attention "memory as state."

## Related
- [[Compressive Transformers]]
- [[Recurrent Memory Transformer]]
- [[Memorizing Transformers]]
- [[Linear Attention As Memory]]
- [[Memory Compression]]
- [[MOC - Memory Architectures]]
