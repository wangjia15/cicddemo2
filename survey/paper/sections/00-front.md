# A Survey of Memory in Large Language Models: Taxonomy, Mechanisms, and Evaluation

## Abstract

Memory — the capacity to store, retain, and recall information — is central to the behavior
and limitations of large language models (LLMs). Yet the term is used for strikingly different
mechanisms: the knowledge compressed into a model's weights, the transient contents of its
context window, the external corpora it retrieves from, the architectural slots that carry
state across time, and the orchestrated stores that let LLM-based agents persist across
sessions. This survey organizes that landscape. We propose a taxonomy of LLM memory along two
axes — *where* information resides and *how long* it persists — yielding five categories:
**parametric**, **contextual/working**, **non-parametric/external**, **architectural**, and
**agent** memory. For each, we describe the underlying mechanisms, representative systems,
and limitations, tracing a line from early memory-augmented neural networks to retrieval
augmentation, long-context Transformers, knowledge editing, and operating-system-style agent
memory. We then survey how memory is evaluated, from efficiency benchmarks to long-context
stress tests and knowledge-editing suites, and highlight the recurring gap between *nominal*
and *effective* memory capacity. We close with open challenges: lifelong and consolidating
memory, principled forgetting, faithful attribution, and evaluation that measures use rather
than mere capacity.

**Keywords:** large language models, memory, retrieval-augmented generation, long context,
knowledge editing, LLM agents, survey.
