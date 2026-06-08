---
title: zsRE
aliases: [zsRE, Zero-Shot Relation Extraction, ZSRE]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

zsRE (Zero-Shot Relation Extraction) is a relation-extraction dataset by Levy et al. that reframes relations as natural-language question templates, originally for extracting facts about unseen relation types [@levy2017]. In the [[Knowledge Editing]] literature it was repurposed as a standard editing benchmark: each fact is a question-answer pair, an edit changes the answer to a new target, and human-written paraphrase questions test whether the edit generalizes. Editing evaluations on zsRE report reliability (the edited answer is produced), generalization (paraphrases also change), and locality (unrelated questions are unaffected). It is used as a complement to [[CounterFact]] by editors such as [[MEND]], [[KnowledgeEditor]], and [[MEMIT]], with zsRE emphasizing question-answering style facts and CounterFact emphasizing counterfactual robustness. Because its targets can be real-world-true, zsRE tests insertion/replacement of plausible facts rather than purely counterfactual ones.

## Related
- [[CounterFact]]
- [[MEND]]
- [[KnowledgeEditor]]
- [[MEMIT]]
- [[Knowledge Editing]]
- [[MOC - Evaluation and Benchmarks]]
