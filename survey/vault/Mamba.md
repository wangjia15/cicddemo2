---
title: Mamba
aliases: [Mamba, Selective State Space Model, Selective SSM, S6]
tags: [llm-memory/architecture, architecture]
status: draft
---

Mamba is a selective state-space model that makes the SSM's recurrence input-dependent, letting the model dynamically decide what to store in and read from its hidden state as a function of each token [@gu2023]. Whereas S4 uses fixed (time-invariant) state-space parameters, Mamba's selection mechanism makes the B, C, and step-size parameters functions of the current input, so the model can selectively propagate or forget information and perform content-aware compression of context into its fixed-size state. Because input-dependent dynamics break the convolutional shortcut used by S4, Mamba is computed with a hardware-aware parallel scan that keeps it efficient and linear in sequence length, with constant-size state at inference (unlike the growing KV cache of attention). It matches or beats similarly-sized Transformers on language, audio, and genomics while handling very long sequences cheaply. As a memory mechanism it offers a compact recurrent state with fast streaming inference, but that fixed-size state still bounds how much can be remembered, and pure SSMs can underperform attention on tasks needing precise long-range copying or associative recall, motivating hybrid SSM-attention designs.

## Related
- [[S4]]
- [[Linear Attention As Memory]]
- [[Memory Compression]]
- [[KV-Cache As Short-Term Memory]]
- [[MOC - Memory Architectures]]
