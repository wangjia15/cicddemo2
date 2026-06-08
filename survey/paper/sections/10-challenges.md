## 10. Open Challenges and Future Directions

The mechanisms surveyed above address memory piecemeal; several problems remain open, and most
of them cut across the taxonomy.

**Lifelong and consolidating memory.** No current category provides true lifelong memory.
Contextual memory is wiped after each sequence; external memory grows monotonically and is never
consolidated; parametric memory is updated only through costly training or brittle edits. Human
memory, by contrast, *consolidates* — transferring salient episodic experience into durable
semantic and procedural form. An analogous loop for LLMs, in which an agent's accumulated
external memory is periodically distilled back into the weights or into compact skills, is
largely unrealized. Editing methods [@meng2023] and skill acquisition [@wang2023voyager] each
capture a fragment of this loop, but a principled, stable consolidation procedure is missing.

**Principled forgetting.** Across categories, forgetting is the weakest operation. External
stores rarely evict; agent memory managers delete heuristically; and in the weights, forgetting
appears mostly as *unwanted* catastrophic interference [@mccloskey1989; @kirkpatrick2017] rather
than as a controllable operation. Yet deliberate forgetting matters for correctness (removing
stale facts), privacy (machine unlearning), and efficiency (bounding memory growth). Making
forgetting selective, verifiable, and non-destructive is an open problem that connects knowledge
editing, continual learning, and agent design.

**Faithfulness and attribution.** Decoupling knowledge from parameters via retrieval was
expected to curb hallucination and enable citation [@lewis2020], but models still ignore,
misread, or override retrieved evidence, and retrieval errors propagate into confident
falsehoods [@ji2023]. Guaranteeing that an answer is *grounded* in the memory it claims to use —
and surfacing that provenance to users — remains unsolved across both retrieval and agent
memory.

**The nominal–effective gap.** Reported memory capacity routinely overstates usable capacity. A
large nominal context window does not imply uniform recall across it [@liu2023lost], and
benchmarks increasingly report an *effective* context length well below the advertised one
[@hsieh2024]. The same gap recurs elsewhere: parametric knowledge that a probe can elicit may
not be used in generation, and an item written to agent memory may never be retrieved when
relevant. Future evaluation should measure memory *use under task pressure*, not storage capacity
in isolation, and should stress multi-hop aggregation rather than single-fact lookup.

**Efficiency and serving.** Memory and cost are inseparable. The KV-cache dominates the memory
footprint of long-context inference, motivating eviction, paging, and sparsity
[@zhang2023h2o; @kwon2023pagedattention]; retrieval shifts cost to an index that must scale to
billions of vectors [@johnson2019; @malkov2018]; and architectural memory trades fidelity for a
bounded state. Co-designing memory mechanisms with the systems that serve them — rather than
treating accuracy and efficiency separately — is an increasingly central concern.

**Unification and interaction.** Finally, the categories are studied in isolation but deployed
together, and their interactions are poorly understood. When a system holds the same fact in its
weights, its context, and its retrieval store, which wins, and how should conflicts be resolved?
A long context window and a retrieval store are partly substitutable; when is each preferable,
and how should they be combined? Cognitive-architecture proposals for agents [@sumers2023] and
emerging memory surveys [@zhang2024memorysurvey] begin to frame these questions, but a predictive
account of how composed memory systems behave is still missing.
