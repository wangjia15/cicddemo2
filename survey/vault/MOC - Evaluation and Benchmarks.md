---
title: MOC - Evaluation and Benchmarks
aliases: [Evaluation MOC, Benchmarks MOC, Long-Context Evaluation MOC]
tags: [llm-memory/parametric-editing, moc]
status: draft
---

# Map of Content: Evaluation and Benchmarks

This cluster collects the **benchmarks and metrics** used to evaluate memory in large language models — both the **parametric knowledge** stored in weights (and edits to it) and the **long-context / working memory** ability to use information held in the context window. Each note explains what the benchmark actually measures and how it differs from its neighbors.

## Probing Parametric Knowledge
- [[LAMA Probe]] — cloze-style probe of how much relational knowledge a pretrained model stores (precision@1).

## Evaluating Knowledge Edits
- [[CounterFact]] — counterfactual targets with paraphrase (generalization), neighborhood (locality), and generation prompts.
- [[zsRE]] — QA-style editing benchmark measuring reliability, generalization, and locality.

## Long-Context: Synthetic Stress Tests
- [[Long Range Arena]] — six diverse tasks (1K-16K) probing architectural long-range modeling plus efficiency.
- [[Needle In A Haystack]] — verbatim retrieval of a planted fact at varying depth/length (a heatmap).
- [[RULER]] — synthetic, scalable multi-needle/tracing/aggregation tasks giving an effective context length.

## Long-Context: Naturalistic Task Suites
- [[LongBench]] — bilingual, multi-task downstream long-context understanding.
- [[ZeroSCROLLS]] — zero-shot understanding and aggregation over long natural documents.
- [[InfiniteBench]] — tasks beyond 100K tokens, pushing the length frontier.

## How They Relate
- Probes (LAMA) and editing benchmarks (CounterFact, zsRE) test **parametric memory** and its modification.
- Synthetic suites (NIAH, RULER, LRA) isolate **retrieval and architectural** capacity with controlled difficulty.
- Naturalistic suites (LongBench, ZeroSCROLLS, InfiniteBench) test **downstream long-context** competence; strong needle-retrieval scores do not imply strong reasoning over long contexts.

## Suggested Reading Order
1. [[LAMA Probe]] → [[CounterFact]] → [[zsRE]]
2. [[Long Range Arena]] → [[Needle In A Haystack]] → [[RULER]]
3. [[LongBench]] → [[ZeroSCROLLS]] → [[InfiniteBench]]

See also [[MOC - Parametric Memory and Editing]] and [[MOC - Retrieval Memory]].
