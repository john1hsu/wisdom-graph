# Wisdom Graph

A growing, citation-backed knowledge graph about wisdom and how to cultivate it: what wisdom is, the science of wise reasoning, self-knowledge, judgment under uncertainty, virtues and character, emotional equanimity, compassion, meaning and the good life, adversity and mortality, wise leadership, and the world's wisdom traditions — Stoic, Aristotelian, Confucian, Daoist, Buddhist and more. A scheduled run researches one new topic, writes it as a practice-ready node with evidenced, typed edges, and only commits it if the validator, the OWL reasoner and the SHACL shapes all agree it is sound.

**Read it online: https://john1hsu.github.io/wisdom-graph/** (rebuilt automatically on every new article by `.github/workflows/pages.yml` from `site/build.py`).

Start with **[`graph/playbook.md`](graph/playbook.md)**: every step-by-step practice, before/after response and self-check question in the graph, grouped by domain.

## Architecture

```
articles/<domain>/<slug>.md          Markdown + YAML frontmatter (one node each)
        │  scripts/kg.py
        ▼
 1. structural validation      citations, uniqueness (shingles + TF-IDF), practice rules, acyclicity
 2. RDF assembly               SKOS + PROV-O + schema.org HowTo + before/after examples, one named graph per article
 3. OWL 2 RL reasoning         inverse / symmetric / transitive properties, domain & range typing
 4. consistency checking       disjoint-class contradictions, domain/range violations
 5. SHACL validation           ontology/shapes.ttl (semantic contract on the exported RDF)
 6. exports + analytics        graph/  (regenerated on every commit; CI fails if stale)
```

| Layer | What | Where |
|---|---|---|
| Ontology | OWL 2 RL classes (Skill, Practice, Framework, Principle, Virtue, Obstacle, Vice, Context, Tradition, Theory, Phenomenon, Work, Study, …) and typed relations (`develops`, `addresses`, `excessOf`/`deficiencyOf` for the doctrine of the mean, `rootedIn` for traditions, `appliedIn`, `undermines`, `challengedBy`, …) with inverses, symmetry, transitivity, domains, ranges and disjointness; aligned with SKOS, PROV-O and schema.org | `ontology/ontology.ttl` |
| Shapes | SHACL: every node defined, sourced, levelled and evidence-rated; practices carry ≥ 3 steps and a before/after example; vices carry a before/after example; skills, practices, virtues, vices and obstacles carry self-check questions | `ontology/shapes.ttl` |
| Nodes | One Markdown article per entity: id, class, hierarchy, prerequisites, evidenced typed edges, steps, before/after example, self-check questions, evidence status, entity links and sources | `articles/<domain>/` |
| Practice playbook | All procedures, before/after examples and self-checks in one place | `graph/playbook.md` |
| Linked data | N-Triples (asserted and OWL-RL inferred), TriG with per-article named graphs and provenance, Turtle-star edge evidence (RDF 1.2), JSON-LD, JSON index | `graph/triples.nt`, `graph/inferred.nt`, `graph/graph.trig`, `graph/edge-evidence.ttls`, `graph/graph.jsonld`, `graph/index.json` |
| Analytics | PageRank, betweenness, Louvain communities, k-core, coverage by type/domain/level/evidence | `graph/stats.md` |
| Frontier | Unwritten nodes ranked by referrers weighted by their centrality, with the **type the reasoner expects** | `graph/frontier.md` |
| Link prediction | Adamic-Adar scores for written nodes that should probably be connected | `graph/suggested-links.md` |
| Competency questions | SPARQL over asserted + inferred triples: highest-leverage practices, toolkit by life situation, teachings by tradition, the doctrine of the mean, contested claims; *gap* queries (unaddressed obstacles and vices, uncultivated skills and virtues, situations without guidance, orphans, unattributed ideas) drive gap-filling runs | `queries/*.rq` → `graph/competency.md` |
| Learning path | Topological layers of the `requires` prerequisite DAG | `graph/learning-path.md` |

## What makes it more than a link list

- **Practice-ready.** Practices have ordered steps (published as schema.org `HowTo`), practices and vices have everyday before/after responses, and skills, practices, virtues, vices and obstacles have self-check questions.
- **Evidence-aware.** Every node has an `evidenceStatus` (robust, mixed, contested, failed-replication, practitioner, theoretical, normative, historical), so empirical findings and philosophical teachings are never confused. Popular advice that outruns its evidence — and misattributed "wisdom quotes" — are flagged and linked to what challenges them.
- **Every typed edge is evidenced.** Each relation cites the source that supports it and carries a confidence, published as RDF-star annotations on the edge.
- **Reasoning, not just storage.** Writers state one direction (`rashness excessOf courage`); the OWL-RL reasoner materialises `hasExcess`, `addressedBy`, symmetric and transitive relations, and types unwritten nodes from property ranges. Contradictory typing fails the build.
- **Self-directing growth.** Runs rotate between depth (frontier), breadth (least-covered domain) and gap (SPARQL competency gaps).
- **Reproducible.** Outputs are byte-for-byte deterministic; CI re-runs tests and the build and fails if `graph/` is stale.

## Usage

```bash
pip install -r requirements.txt
python3 scripts/kg.py check                          # validate + reason + SHACL
python3 scripts/kg.py build                          # ...and regenerate graph/
python3 scripts/kg.py similar "phronesis"            # duplicate check for a candidate topic
python3 scripts/kg.py new emotions-and-equanimity negative-visualization Practice   # scaffold
python3 scripts/kg.py query queries/05-toolkit-by-situation.rq      # or an inline SPARQL string
python3 -m pytest -q tests                           # end-to-end tests on fixture articles
```

Steer what gets written by editing `topics/seeds.yaml`. The run playbook is `CLAUDE.md`; the article format is `SCHEMA.md`. The `.nt`, `.trig` and `.jsonld` exports load into Apache Jena/Fuseki, GraphDB, Oxigraph, rdflib, or Neo4j via n10s; `.ttls` needs an RDF 1.2 / RDF-star aware store.
