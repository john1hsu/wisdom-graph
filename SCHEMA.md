# Article schema

Each article is one **node**: `articles/<domain>/<slug>.md`, where the filename equals the id's slug and `<domain>` is a key in `topics/seeds.yaml`. Scaffold one with `python3 scripts/kg.py new <domain> <slug> <Type>`, which pre-fills the fields and sections its class needs.

```markdown
---
id: wg:self-distancing                   # wg: + lowercase-hyphen slug; never changes
type: Practice                           # most specific class from ontology/ontology.ttl
title: Self-distancing
aliases: [distanced self-talk, illeism]
domain: self-knowledge                   # key in topics/seeds.yaml (becomes a SKOS ConceptScheme)
summary: >-                              # 1–2 sentence definition (skos:definition)
  Reflecting on your own situation as an outside observer would, for example by using your name or the third person.
level: introductory                      # introductory | intermediate | advanced
evidenceStatus: mixed                    # see table below
broader: [wg:reflective-practices]       # skos:broader, 1–3; must stay acyclic
related: [wg:view-from-above]            # skos:related (symmetric)
requires: [wg:perspective-taking]        # learning prerequisites (transitive, acyclic) -> graph/learning-path.md
relations:                               # typed edges: EVERY one cites a source id below
  - {predicate: addresses, object: wg:solomons-paradox, source: s1, confidence: high}
  - {predicate: develops, object: wg:wise-reasoning, source: s1}               # confidence defaults to medium
  - {predicate: appliedIn, object: wg:interpersonal-conflict, source: s2}
  - {predicate: introducedBy, object: wg:ethan-kross, source: s2}
steps:                                   # Practice: >= 3 ordered steps -> schema:HowTo
  - Pause before reacting to the situation that has upset you.
  - Describe it to yourself in the third person, using your own name.
  - Ask what you would advise a friend to do in exactly this position.
example:                                 # Practice, Vice: required before/after responses
  situation: A colleague takes credit for your work in a team meeting.
  before: "I'm calling this out in front of everyone, right now."
  after: "What would Sam tell a friend here? Raise it with them privately first, and calmly."
  why: Stepping outside the moment shifts attention from the sting to the outcome you actually want.
selfCheck:                               # Skill, Practice, Virtue, Vice, Obstacle: >= 2, each ends with "?"
  - Did I look at this as an outsider would before acting?
  - Would I give a friend the advice I'm about to follow?
sameAs: []                               # optional entity links: Wikidata QIDs or https IRIs (incl. sibling graphs) -> skos:exactMatch
sources:                                 # >= 3; >= 2 strong; >= 1 scholarly
  - id: s1
    title: "Solomon's paradox: Self-distancing eliminates the self-other asymmetry in wise reasoning"
    publisher: Psychological Science (SAGE)
    url: https://journals.sagepub.com/doi/...
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
modified: 2026-11-20                     # optional; set when an article is revised
---

# Self-distancing

Prose with footnote citations after each claim.[^s1]

## Origin
## Why it matters
## How to apply it         (Practice)              ## Common mistakes     (Practice)
## What good looks like    (Skill, Virtue)         ## How to practise it  (Skill, Virtue)
## How to spot it          (Obstacle, Vice)        ## How to fix it       (Obstacle, Vice)
## What wisdom looks like here (Context)           ## Pitfalls            (Context)
## Key teachings           (Tradition)             ## Common misreadings  (Tradition)
## Evidence                (Obstacle, Phenomenon, Theory: key studies, effect sizes, replications)
## Connections             (always: explain each edge in prose, with citations)
## Sources                 (always)
[^s1]: Grossmann & Kross (2014), "Exploring Solomon's paradox", *Psychological Science*. https://... (accessed 2026-11-12)
```

Class-specific headings are enforced; `## Origin` and `## Why it matters` are expected for every article. When a classic text is the source, cite the passage (book and section) in the footnote.

## Classes (`type`)

| Class | Use for |
|---|---|
| `Concept` | general ideas: practical wisdom (phronesis), theoretical wisdom (sophia), eudaimonia, meaning in life |
| `Skill` | learnable capacities of wise reasoning: perspective-taking, recognising the limits of one's knowledge, integrating viewpoints, emotional regulation |
| `Practice` | concrete exercises with steps: self-distancing, the evening review, negative visualization, the view from above, a virtue journal, loving-kindness meditation |
| `Framework` | structuring models: Berlin wisdom paradigm, balance theory of wisdom, three-dimensional wisdom model, the Noble Eightfold Path, VIA character strengths |
| `Principle` | teachings and maxims: know thyself, the dichotomy of control, the doctrine of the mean, the Golden Rule, impermanence |
| `Virtue` | traits of character: prudence, intellectual humility, temperance, courage, justice, patience, equanimity, compassion, gratitude |
| `Obstacle` | psychological or situational obstacles: Solomon's paradox, egocentric bias, the end-of-history illusion, hedonic adaptation, self-deception |
| `Vice` | unwise habits and failings: hubris, rashness, cowardice, dogmatism, rumination, cynicism, intemperance |
| `Context` | life situations that call for wisdom: interpersonal conflict, a major life decision, grief and loss, failure, ageing, leading others, giving advice |
| `Tradition` | wisdom traditions: Stoicism, Aristotelian virtue ethics, Confucianism, Daoism, Buddhism, Epicureanism, Hebrew wisdom literature, Vedanta |
| `Theory` | academic theories: socioemotional selectivity theory, Erikson's psychosocial stages, construal level theory |
| `Phenomenon` | observed patterns: the positivity effect in ageing, post-traumatic growth, the wisdom of crowds |
| `Field` | disciplines: virtue ethics, positive psychology, lifespan developmental psychology, contemplative science |
| `Person`, `Organization`, `Work`, `Study`, `Event` | thinkers and researchers, institutions, classic texts and landmark books, landmark studies, milestones |

Disjointness is declared (problems — `Obstacle`, `Vice` — vs. remedies — `Skill`, `Practice`, `Principle`, `Virtue`; `Context` vs. `Tradition`; concepts vs. people, works and studies). The reasoner types unwritten nodes from edge ranges; two edges that imply incompatible types fail the build.

## Predicates (`relations[].predicate`)

| Predicate | Meaning | Constraint | Inferred inverse |
|---|---|---|---|
| `partOf` | component of | transitive | `hasPart` |
| `requires`* | learning prerequisite | transitive, acyclic | `prerequisiteOf` |
| `instanceOf` | variant of | | `hasInstance` |
| `contrastsWith`, `confusedWith`, `alternativeTo`, `complements` | comparisons | symmetric | itself |
| `develops` | practice or teaching that cultivates a capacity | Practice/Framework/Principle → Skill/Virtue | `developedBy` |
| `addresses` | counters a problem | Practice/Framework/Principle/Skill/Virtue → Obstacle/Vice | `addressedBy` |
| `excessOf`, `deficiencyOf` | a vice as too much / too little of a virtue (doctrine of the mean) | Vice → Virtue | `hasExcess`, `hasDeficiency` |
| `appliedIn` | used in a life situation | → Context | `benefitsFrom` |
| `rootedIn` | taught by a wisdom tradition | → Tradition | `teaches` |
| `causes` | leads to | | `causedBy` |
| `undermines` | damages (judgment, well-being, relationships…) | Obstacle/Vice → | `underminedBy` |
| `explainedBy` | mechanism or theory behind | | `explains` |
| `demonstratedBy` | shown by a landmark study | → Study | `demonstrates` |
| `supportedBy`, `challengedBy` | evidence for / critique, failed replication, misattribution, myth-busting | | `supports`, `challenges` |
| `introducedBy` | named, taught or popularised by | → Person | `introduced` |
| `introducedIn` | introduced in | → Work | `introduces` |
| `authoredBy` | author of a work | Work → Person | `authored` |
| `influencedBy` | intellectual influence | | `influenced` |
| `studiedIn` | studied in a discipline | → Field | |

\* `requires` is written as its own list, not under `relations`. Never write inverses yourself; the reasoner materialises them in `graph/inferred.nt`. If you need a new predicate or class, add it to `ontology/ontology.ttl` with a label, any domain/range, and its inverse/characteristics in the same commit.

## Evidence status

| value | meaning | rule |
|---|---|---|
| `robust` | empirical finding that has replicated well | needs a peer-reviewed or primary study |
| `mixed` | real but smaller, moderated or context-dependent effects | needs a peer-reviewed or primary study |
| `contested` | active dispute, or a claim widely repeated beyond its evidence | needs a study + a `challengedBy` relation |
| `failed-replication` | large replications failed to reproduce the original effect | needs a study + a `challengedBy` relation |
| `practitioner` | expert or practitioner advice with little formal testing | not allowed for `Theory` |
| `theoretical` | an academic model or theory, judged by explanatory use | |
| `normative` | a philosophical or traditional teaching, judged by argument and long practice rather than experiment (the dichotomy of control, the doctrine of the mean) | not allowed for `Phenomenon` or `Study` |
| `historical` | mainly of historical interest (people, texts, events, traditions) | |

A teaching can be `normative` and still have empirical work on a modern version of it (e.g. Stoic-inspired reappraisal); say so in `## Evidence` or the prose and link the study with `supportedBy` / `challengedBy`.

## Source types

| type | strong | scholarly | examples |
|---|---|---|---|
| `peer-reviewed` | yes | yes | *Psychological Science*, *PNAS*, *Perspectives on Psychological Science*, *Psychology and Aging*, *J. Happiness Studies* (DOI page) |
| `primary` | yes | yes | the original study, or a scholarly edition or translation of a classic text (Perseus, MIT Internet Classics Archive, university press) |
| `textbook` | yes | yes | academic philosophy, ethics, lifespan-development and positive-psychology textbooks |
| `academic` | yes | yes | Chicago Center for Practical Wisdom, Berkeley Greater Good Science Center, university course and research-centre pages |
| `government` | yes | yes | NIH / National Institute on Aging, NCCIH |
| `intergovernmental` | yes | yes | UNESCO, WHO |
| `scholarly-encyclopedia` | yes | yes | Stanford / Internet Encyclopedia of Philosophy |
| `practitioner-journal` | yes | no | *Harvard Business Review*, *MIT Sloan Management Review*, *Psyche* essays by researchers |
| `institutional` | yes | no | VIA Institute on Character, American Psychological Association |
| `encyclopedia` | yes | no | Britannica |
| `preprint`, `news`, `community` | no | no | context only, never the sole support for a claim |

**Banned:** Wikipedia (and mirrors), Wikiquote, wikiHow, Quora, Fandom, quotation aggregators (BrainyQuote, Goodreads quotes, AZ Quotes, Quotefancy…), content farms, SEO listicles and AI-generated pages.

## Enforcement summary (`scripts/kg.py check`)

1. **Structure:** required fields, enums, id/filename/folder agreement, known domain, dates.
2. **Citations:** ≥ 3 sources, ≥ 2 strong, ≥ 1 scholarly, empirical claims backed by a study, https only, no banned or duplicate URLs, every source cited, every substantive paragraph cited, every typed edge cites a source.
3. **Practice rules:** class-specific sections; ≥ 3 steps for practices; before/after responses for practices and vices (before ≠ after, with a reason); ≥ 2 self-check questions for skills, practices, virtues, vices and obstacles; `challengedBy` for disputed claims; no `normative` status for empirical classes.
4. **Graph rules:** ≥ 3 edges and ≥ 1 typed relation per node, domain/range on written targets, no cycles in `broader` / `requires` / `partOf`.
5. **Uniqueness:** no shared ids, titles or aliases; no near-identical titles; no copied text (5-gram shingles); no same-topic rewrite (TF-IDF cosine ≥ 0.80; ≥ 0.60 warns).
6. **Reasoning:** OWL 2 RL closure; any node inferred into two disjoint classes fails.
7. **SHACL:** `ontology/shapes.ttl` over the exported RDF with RDFS inference.
