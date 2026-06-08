---
title: StreamingLLM And Attention Sinks
aliases: [StreamingLLM, Attention Sinks, Attention Sink]
tags: [llm-memory/context, method]
status: draft
---

StreamingLLM enables a pretrained LLM to process effectively unbounded streams of text with a fixed-size KV-cache by exploiting "attention sinks" — the observation that models dump large amounts of attention onto the first few tokens regardless of their semantic relevance [@xiao2023streamingllm]. When a naive sliding window evicts these initial tokens, perplexity explodes; StreamingLLM fixes this by always keeping a few initial sink tokens in the cache together with the most recent window of tokens. This lets generation continue stably over millions of tokens without fine-tuning, treating the cache as a rolling short-term memory. The crucial limitation is that it does not extend the model's true context: information about the discarded middle tokens is genuinely lost, so StreamingLLM supports endless fluent generation but not long-range recall of evicted content. It is one of several KV-cache management strategies alongside [[H2O Heavy Hitter Oracle]].

## Related
- [[KV-Cache As Short-Term Memory]]
- [[H2O Heavy Hitter Oracle]]
- [[Paged Attention And vLLM]]
- [[Lost In The Middle]]
- [[MOC - Context Memory]]
