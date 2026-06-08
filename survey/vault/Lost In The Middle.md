---
title: Lost In The Middle
aliases: [Lost in the Middle, Lost-in-the-Middle, Positional Bias]
tags: [llm-memory/context, concept]
status: draft
---

"Lost in the Middle" names the empirical finding that long-context LLMs use their context window unevenly: they retrieve information placed near the beginning or the end of the input far more reliably than information buried in the middle, producing a U-shaped accuracy curve over document position [@liu2023lost]. The effect holds even for models explicitly trained or extended to long contexts, showing that a large nominal window does not guarantee uniform access to its contents — a gap between a model's advertised context length and its *effective* working memory. The bias is thought to arise from a mix of positional encoding behavior, attention sinks on early tokens, and recency effects from autoregressive training. Practically, it means simply enlarging the context window via [[Position Interpolation]] or [[YaRN]] can preserve fluency while leaving mid-context recall weak, so document ordering and retrieval ranking materially affect answer quality. The phenomenon motivates needle-in-a-haystack style probes that test retrieval as a function of position, and it sharpens the distinction in [[Length Generalization And Extrapolation]] between low perplexity and genuine long-range recall.

## Related
- [[Context Window As Working Memory]]
- [[Length Generalization And Extrapolation]]
- [[StreamingLLM And Attention Sinks]]
- [[Position Interpolation]]
- [[YaRN]]
- [[MOC - Context Memory]]
