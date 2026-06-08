---
title: Neural Turing Machine
aliases: [NTM, Neural Turing Machines]
tags: [llm-memory/architecture, architecture]
status: draft
---

The Neural Turing Machine couples a neural network controller (typically an LSTM) to an external memory matrix through differentiable read and write "heads," giving the network something analogous to the working memory and addressable tape of a computer [@graves2014]. Memory access is fully differentiable: heads emit weightings over memory rows produced by combining content-based addressing (matching a key against stored vectors by cosine similarity) with location-based addressing (shifting along memory rows), so the whole system can be trained end-to-end by gradient descent. Writes use erase-and-add vectors in the style of an LSTM gate, letting the controller selectively overwrite memory. NTMs learned simple algorithms such as copying, repeat-copy, sorting, and associative recall, generalizing to longer sequences than seen in training, which standard RNNs struggle to do. Limitations include unstable and difficult training, sensitivity to hyperparameters, an inability to allocate or free memory cleanly (slots can collide or be reused unintentionally), and poor scaling of the dense addressing to large memories. These shortcomings, especially memory allocation, were addressed by its successor, the Differentiable Neural Computer.

## Related
- [[Differentiable Neural Computer]]
- [[Memory Networks]]
- [[Content-Based Addressing]]
- [[End-to-End Memory Networks]]
- [[MOC - Memory Architectures]]
