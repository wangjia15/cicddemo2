---
title: LAMA Probe
aliases: [LAMA, LAnguage Model Analysis, Knowledge Probing]
tags: [llm-memory/parametric-editing, benchmark]
status: draft
---

LAMA (LAnguage Model Analysis) is a probe introduced by Petroni et al. to measure how much factual and commonsense knowledge a pretrained language model stores in its parameters, without any fine-tuning [@petroni2019]. It converts relational facts (subject, relation, object triples) from sources like Wikidata/T-REx, ConceptNet, and SQuAD into natural-language cloze statements (e.g. "Dante was born in [MASK]") and checks whether the model ranks the correct object highest. The headline finding was that models such as BERT already recall a substantial amount of relational knowledge, rivaling some systems built with explicit supervision, which reframed language models as soft knowledge bases. LAMA measures parametric recall accuracy (typically precision-at-1) and is sensitive to how prompts are phrased, motivating later work on prompt robustness. It is the canonical evaluation of [[Parametric Memory]] and the testbed used by [[Knowledge Neurons]].

## Related
- [[Parametric Memory]]
- [[Knowledge Neurons]]
- [[zsRE]]
- [[CounterFact]]
- [[MOC - Evaluation and Benchmarks]]
