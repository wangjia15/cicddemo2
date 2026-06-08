# Figures — A Survey of Memory in Large Language Models

This file holds all Mermaid figures for the survey. Each figure has an exact label heading
(referenced by section writers), a one-sentence caption, and a fenced `mermaid` block.

### Figure: LLM Memory Taxonomy

The five top-level categories of LLM memory with representative methods in each.

```mermaid
mindmap
  root((LLM Memory))
    Parametric
      FFN Key-Value Memory
      ROME
      MEMIT
      MEND
    Contextual Working
      KV-Cache
      RoPE and ALiBi
      StreamingLLM
      FlashAttention
    External Retrieval
      RAG
      REALM
      RETRO
      kNN-LM
    Architectural
      Transformer-XL
      RMT
      NTM and DNC
      Infini-attention
    Agent
      MemGPT
      Generative Agents
      Reflexion
      Voyager
```

### Figure: Memory Timeline

A decade of memory milestones for neural sequence models, from Memory Networks to long-context LLMs.

```mermaid
timeline
    title Memory Milestones 2014-2024
    2014-2015 : Memory Networks : Neural Turing Machine
    2017 : Transformer
    2019 : Transformer-XL
    2020 : REALM : RAG : kNN-LM
    2022 : RETRO : Recurrent Memory Transformer
    2023 : MemGPT : Generative Agents
    2024 : Infini-attention : Long-context LLMs
```

### Figure: KV-Cache and Attention-Sink Flow

How tokens build the KV-cache and how eviction, attention sinks, and paging bound its growth.

```mermaid
flowchart TD
    T[Input tokens] --> A[Self-attention layer]
    A --> KV[KV-cache grows per token]
    KV --> B{Cache budget exceeded?}
    B -- No --> KEEP[Keep full cache]
    B -- Yes --> M[Cache management]
    M --> SINK[Keep attention sink tokens]
    M --> WIN[Keep recent window]
    M --> EVICT[Evict heavy hitters policy]
    M --> PAGE[Paged attention blocks]
    SINK --> O[Bounded cache for next step]
    WIN --> O
    EVICT --> O
    PAGE --> O
    KEEP --> O
```

### Figure: RAG Pipeline

The retrieve-then-generate pipeline from query through ANN search to a grounded answer.

```mermaid
flowchart LR
    Q[User query] --> E[Query encoder]
    E --> V[ANN search over vector DB]
    C[(Document chunks)] --> EMB[Chunk embeddings]
    EMB --> V
    V --> R[Top-k retrieved chunks]
    R --> P[Prompt with context]
    Q --> P
    P --> LLM[LLM generator]
    LLM --> ANS[Grounded answer]
```

### Figure: Segment-Level Recurrence

Carrying or compressing a memory state across fixed-length segments to extend effective context.

```mermaid
graph LR
    S1[Segment 1] --> B1[Transformer block]
    B1 --> M1[Memory state 1]
    M1 --> B2[Transformer block]
    S2[Segment 2] --> B2
    B2 --> M2[Memory state 2]
    M2 --> COMP[Compress old memory]
    COMP --> B3[Transformer block]
    S3[Segment 3] --> B3
    B3 --> M3[Memory state 3]
```

### Figure: Agent Memory Architecture

An LLM agent with working and core memory over long-term episodic, semantic, and procedural stores, with retrieval scoring and read/write/forget operations.

```mermaid
flowchart TD
    AGENT[LLM agent reasoning] --> WM[Working memory context window]
    WM --> CORE[Core memory persona blocks]
    AGENT --> RET[Retrieval scoring]
    RET --> EPI[(Episodic store)]
    RET --> SEM[(Semantic store)]
    RET --> PROC[(Procedural skill store)]
    RET -. recency importance relevance .-> WM
    EPI -- read --> WM
    SEM -- read --> WM
    PROC -- read --> WM
    AGENT -- write --> EPI
    AGENT -- write --> SEM
    AGENT -- write --> PROC
    AGENT -- forget --> EPI
    REFLECT[Reflection consolidation] --> SEM
    EPI --> REFLECT
```
