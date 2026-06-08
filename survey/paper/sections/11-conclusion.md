## 11. Conclusion

Memory is not a single feature of large language models but a family of mechanisms operating at
different locations and timescales. In this survey we organized that family along two axes —
where information resides and how long it persists — into five categories: parametric,
contextual/working, non-parametric/external, architectural, and agent memory. Reading the field
through this lens reveals a coherent story rather than a scatter of techniques. Knowledge begins
compressed and immovable in the weights; the context window offers high-fidelity but volatile
and bounded working memory; retrieval externalizes knowledge so it can be inspected and updated;
architectural mechanisms extend temporal reach by carrying compressed state; and agent systems
wrap the model in explicit, persistent stores with read, write, and forget policies.

Several threads tie the categories together: content-based addressing as a shared retrieval
primitive, the recurring trade-off between compression and fidelity, and a spectrum of
updatability that explains why retrieval and editing have become the dominant means of keeping
models current. The same lens also clarifies where progress is most needed — lifelong
consolidation, principled forgetting, faithful attribution, and evaluation that measures the
*use* of memory rather than its raw capacity, where nominal and effective limits still diverge
sharply.

As LLMs move from single-turn predictors toward persistent, long-horizon agents, memory is
likely to be the axis along which the most consequential advances occur. We hope the taxonomy
and synthesis offered here give researchers a shared map: a way to place a new method among its
neighbors, to see which trade-offs it accepts, and to identify which of memory's open problems
it leaves unsolved.
