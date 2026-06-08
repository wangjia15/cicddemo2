# LLM Memory Survey

An English academic survey on **memory in Large Language Models**, produced by the Claude Code
agent team in `.claude/agents/`. The knowledge base is a self-contained **Obsidian** vault; the
manuscript cites it and uses **Mermaid** figures.

## Layout

```
survey/
  vault/                 # Obsidian knowledge base (84 atomic notes + 6 MOCs)
  paper/
    Survey Outline.md    # taxonomy + section plan (source of truth)
    references.bib       # 64 verified BibTeX entries (keys match [@cite] in notes & paper)
    sections/            # one markdown file per section (00 front … 11 conclusion)
    figures/figures.md   # 6 Mermaid figures (validated via mermaid-cli)
    paper.md             # ASSEMBLED MANUSCRIPT (sections + figures + reference list)
```

## The manuscript

`paper/paper.md` is the full survey (~14,900 words): Abstract, 11 sections, 6 embedded Mermaid
figures, and a 64-entry reference list. It organizes LLM memory into five categories —
**parametric, contextual/working, non-parametric/external, architectural, and agent** — and
covers mechanisms, representative systems, evaluation, and open challenges.

Citations use Pandoc-style `[@key]`. To render with a formatted bibliography:

```bash
pandoc paper/paper.md --citeproc --bibliography=paper/references.bib -o paper.pdf
```

Mermaid figures render in Obsidian, GitHub, and any Mermaid-aware viewer.

## The Obsidian vault

`vault/` is a browsable knowledge graph: one concept per note, YAML frontmatter, `[[wikilinks]]`,
and six Maps-of-Content (`MOC - *.md`) starting points. Open the `vault/` folder as an Obsidian
vault to explore the graph.

## Reproducing / extending

The team that built this lives in `.claude/agents/` (see its README). To extend a topic, have
`research-scout` produce a findings brief, `wiki-curator` add atomic notes, then `section-writer`
+ `diagram-designer` + `citation-manager` update the paper, and `survey-editor` review.
