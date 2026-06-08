## 3. A Taxonomy of LLM Memory

We organize the field along two questions: **where** does the information physically reside,
and **how long** does it persist relative to a single forward pass? These two axes separate
mechanisms that are otherwise easy to conflate — for instance, a fact baked into the weights
and the same fact pasted into the prompt are both "memory," but they differ in location
(parameters vs. activations), persistence (permanent vs. single inference), and updatability
(requires training vs. trivially editable). Crossing the axes yields five categories, summarized
in Figure: LLM Memory Taxonomy and Table 1.

**(1) Parametric memory.** Knowledge stored implicitly in the model's weights, acquired during
pretraining. It is permanent across inferences, dense and compressed, and accessed without any
explicit lookup — but it is opaque, costly to update, and prone to becoming stale. The
feed-forward layers of the Transformer behave like key–value memories that store such
associations [@geva2021], and a line of work locates and rewrites individual facts in the
weights [@meng2022]. *(Section 4.)*

**(2) Contextual / working memory.** The transient contents of the context window, realized in
the attention activations and the KV-cache. This is the model's working memory: high-fidelity
and immediately usable, but volatile (it vanishes after the sequence), bounded in size, and
quadratically expensive in length [@vaswani2017]. Positional encodings, efficient attention,
KV-cache management, and context-extension methods all push on these limits, yet effective use
still degrades for information far from the prompt's edges [@liu2023lost]. *(Section 5.)*

**(3) Non-parametric / external memory.** Knowledge kept outside the model in a corpus or vector
store and pulled in at inference time via retrieval [@lewis2020]. It is explicit, inspectable,
and easily updated — add or remove a document without retraining — and supports attribution, at
the price of dependence on retrieval quality. *(Section 6.)*

**(4) Architectural memory.** Memory built into the network as recurrent state or learnable
slots that carry information across segments or steps, rather than residing in a flat context
window. This lineage runs from external-memory neural networks with differentiable read/write
[@graves2014] to segment-recurrent and compressive Transformers [@dai2019; @rae2020] and
fixed-size recurrent state in state-space models. It extends the temporal reach of the model but
trades fidelity for a bounded memory footprint. *(Section 7.)*

**(5) Agent memory.** Memory as an orchestrated system around the LLM: explicit stores for
episodic, semantic, and procedural content, with policies for what to write, when to retrieve,
how to score relevance, and when to forget [@packer2023; @park2023]. It targets persistence
across sessions and long-horizon tasks and draws directly on cognitive analogies, but the
read/write/forget policies are largely heuristic. *(Section 8.)*

**Cross-cutting threads.** Three ideas recur across categories and are worth tracking. First,
*content-based addressing* — retrieving by similarity rather than by location — appears in
attention, in differentiable memories, and in vector retrieval alike. Second, the
*compression–fidelity trade-off*: any mechanism that summarizes the past into a bounded state
(compressive Transformers, recurrent state, rolling summaries) buys reach at the cost of detail.
Third, *updatability*: the categories form a spectrum from hardest to update (parametric) to
trivially updatable (external/context), which largely explains why retrieval and editing have
become the dominant routes to keeping LLM knowledge current.

These categories are deliberately not mutually exclusive in practice — a deployed system may
combine a retrieval store, a long context window, and an agent memory manager on top of fixed
parametric knowledge. The taxonomy describes mechanisms, not products; real systems compose
them, and Section 10 returns to how they interact.

*Table 1. The five categories of LLM memory.*

| Category | Where it resides | Persistence | Updatable? | Representative work |
|---|---|---|---|---|
| Parametric | Model weights | Permanent | Hard (training/editing) | FFN-as-memory [@geva2021], ROME [@meng2022] |
| Contextual / working | Activations, KV-cache | Single inference | Trivial (change prompt) | Long-context attention [@beltagy2020longformer], StreamingLLM [@xiao2023streamingllm] |
| Non-parametric / external | Corpus / vector store | Until edited | Easy (edit corpus) | RAG [@lewis2020], RETRO [@borgeaud2022] |
| Architectural | Recurrent state / memory slots | Across segments | Via mechanism | NTM [@graves2014], Transformer-XL [@dai2019] |
| Agent | External orchestrated stores | Across sessions | Explicit read/write | MemGPT [@packer2023], Generative Agents [@park2023] |
