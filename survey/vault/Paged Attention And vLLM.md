---
title: Paged Attention And vLLM
aliases: [PagedAttention, Paged Attention, vLLM]
tags: [llm-memory/context, method]
status: draft
---

PagedAttention, introduced in the vLLM serving system, manages the KV-cache the way an operating system manages virtual memory: it splits each sequence's cache into fixed-size blocks ("pages") that can be stored non-contiguously and looked up through a block table [@kwon2023pagedattention]. This nearly eliminates the internal and external memory fragmentation caused by pre-allocating contiguous cache for each request's maximum length, and it lets identical blocks (e.g., a shared prompt prefix or beam-search branches) be shared via copy-on-write. The result is much higher batch sizes and serving throughput for long-context workloads without changing model outputs. It is an infrastructure-level technique that targets the memory-management problem of the KV-cache rather than reducing the cache's logical size, so it composes with eviction methods like H2O and StreamingLLM. Its limitations are added indirection/bookkeeping for block tables and that it does not by itself extend context length or improve recall.

## Related
- [[KV-Cache As Short-Term Memory]]
- [[StreamingLLM And Attention Sinks]]
- [[H2O Heavy Hitter Oracle]]
- [[FlashAttention]]
- [[MOC - Context Memory]]
