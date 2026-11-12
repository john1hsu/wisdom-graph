# Wisdom Graph — run playbook

This repo is a citation-backed, reasoner-checked knowledge graph about wisdom and how to cultivate it: what wisdom is, the science of wise reasoning, self-knowledge and reflection, judgment and decisions under uncertainty, virtues and character, emotional wisdom and equanimity, compassion and wisdom with others, meaning and the good life, adversity, loss and mortality, wisdom at work and in leadership, the world's wisdom traditions, and the thinkers, texts and studies behind them. A scheduled run adds **exactly one new, unique article** per run. Every article must help the reader *judge, decide or live* a little more wisely. Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
pip install -r requirements.txt --break-system-packages -q
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md`, `graph/competency.md` and `topics/seeds.yaml`. `graph/index.json` lists every node (ids, titles, aliases, edges, steps, examples, source URLs).

## 2. Pick the topic (graph-driven)
Use the current UTC hour modulo 3:
- **0 → depth.** Take the top node in `graph/frontier.md` that fits a domain, **skipping any node that would belong to the domain with the most articles** ("Domain coverage" in `graph/stats.md`; on a tie for most, skip all tied domains), so one domain's dense cross-links can't snowball into a lopsided graph. Use its *Expected type* (inferred by the reasoner) as the article's `type` unless it is clearly wrong.
- **1 → breadth.** Take the domain at the top of "Domain coverage" in `graph/stats.md` (fewest articles; skip the domain of the most recent commit on ties) and pick an unwritten seed or another important topic in it.
- **2 → gap.** Take the first row of the first non-empty *(gap)* section in `graph/competency.md` and write the article that closes it (a practice or teaching that counters an unaddressed obstacle or vice, a practice that cultivates a skill or virtue, guidance for a life situation, the person, text or tradition behind an unattributed idea).
- If the chosen mode yields nothing (as on the first runs, when the frontier is empty), fall back to breadth.

Then prove it is unique:
```bash
python3 scripts/kg.py similar "<candidate title>"
```
If any score ≥ 0.5, or an existing title/alias names the same thing, pick a different topic. Never write a second article on an existing subject — not a rename, a sub-angle that restates it, a translation (phronesis vs. practical wisdom, ataraxia vs. tranquility), a transliteration (Laozi vs. Lao Tzu, Dao vs. Tao) or a synonym. Record alternate names and original-language terms as `aliases`.

Sibling graphs cover neighbouring ground: cognitive biases, fallacies and argument evaluation belong to `john1hsu/critical-thinking-graph`, and listening, feedback and difficult-conversation techniques to `john1hsu/communication-graph`. Write here only when the topic is about wisdom itself (e.g. intellectual humility as a virtue, Solomon's paradox, wise counsel), and link the sibling article with `sameAs` (its `https://github.com/john1hsu/<repo>/id/<slug>` IRI) when it is the same concept.

## 3. Research
- Run several web searches and read the actual pages (WebFetch). Don't rely on snippets or memory.
- Collect 3–6 credible sources: ≥ 1 scholarly and ≥ 2 strong (see `SCHEMA.md`). Prefer peer-reviewed research and meta-analyses (Baltes and Staudinger, Sternberg, Ardelt, Grossmann, Jeste, Kross), the Stanford and Internet Encyclopedias of Philosophy, scholarly translations of classic texts (Perseus, the MIT Internet Classics Archive, university presses), university research centres (Chicago Center for Practical Wisdom, Berkeley Greater Good Science Center) and *HBR* / *MIT SMR* articles by researchers. **Never cite Wikipedia, Wikiquote, wikiHow or quotation sites** (BrainyQuote, Goodreads quotes, AZ Quotes…) or the other banned sources.
- Every URL you cite must be one you opened this run. Never invent a URL, DOI or Wikidata id. Only add `sameAs: [wd:Q…]` if you opened that Wikidata page and it is the same concept.
- **Quotations and attributions.** Famous "wisdom quotes" are very often misattributed or apocryphal (to Confucius, the Buddha, Lincoln, Einstein…). Attribute a saying only if a primary text or a scholarly source confirms it, cite the passage (book and section, e.g. *Meditations* 4.3), and say when a popular version is a paraphrase or a misattribution.
- A lot of wisdom and self-help advice outruns its evidence. Check it: look for replications and meta-analyses, and set `evidenceStatus` honestly. Popular claims that outrun their evidence (e.g. universal post-traumatic growth, the "ikigai" Venn diagram as a Japanese tradition) are `contested` or `failed-replication`, with a `challengedBy` edge. Teachings of a tradition judged by argument and long practice rather than experiment are `normative`; untested expert advice is `practitioner`.
- Represent traditions accurately and respectfully, in their own terms and with scholarly sources; note where schools within a tradition disagree, and where a modern popular version differs from the original. Describe teachings — don't preach, rank traditions or tell readers what to believe.
- Paraphrase. No quotation longer than 15 words; at most one quote per source.

## 4. Write the node
```bash
python3 scripts/kg.py new <domain> <slug> <Type>   # scaffold with the fields and sections the class requires
```
- 400–1,000 words, for a thoughtful general reader: definition, origin, why it matters, how to practise or apply it, common mistakes or misreadings, evidence and limits, and **Connections**. Where relevant, note how it shows up at work, in relationships and across cultures and traditions.
- `steps` are concrete and imperative. `example` is a realistic everyday or workplace situation with a less wise and a wiser response, and a short "why". `selfCheck` questions are ones a reader could ask themselves right before or after a real decision, conflict or setback.
- Every substantive paragraph carries footnote citations `[^sN]`; list every source in `## Sources`.
- Edges: 1–3 `broader`, `related` as needed, `requires` for genuine prerequisites, and ≥ 1 (ideally 2–5) typed `relations`, **each citing the source that supports it** and a confidence. Use `rootedIn` to tie a teaching or practice to its tradition, and `excessOf` / `deficiencyOf` to place a vice on either side of a virtue. Link to existing ids wherever they fit (`graph/index.json`); new target ids are fine and join the frontier. Match each predicate's domain and range (`SCHEMA.md`). Never write inverses — the reasoner adds them.
- If a needed class or predicate is missing, add it to `ontology/ontology.ttl` (label, domain/range, inverse/characteristics) in the same commit. Keep the ontology small; reuse first.
- Back-links: if `graph/suggested-links.md` or the new node shows an existing article should point to it, you may add the id to that article's `related` (or a sourced typed relation). Don't otherwise rewrite existing articles.

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every problem (structure, citations, reasoning contradictions, SHACL) and re-run until OK
git add -A
git commit -m "Add <Title> (<domain>, <mode> run)"
git pull --rebase origin main && python3 scripts/kg.py build && git push origin main
```
If the push is rejected, pull --rebase, rebuild, and push again (once). Commit regenerated `graph/` files with the article; CI fails if they are stale.

## Don'ts
- Don't add more than one article per run, delete articles, or rewrite history.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open, attach a source to an edge it doesn't support, or attribute a quotation you couldn't verify.
- Don't hand-edit anything in `graph/`.
- Don't proselytise, rank traditions or present one religion's or school's claims as settled fact; describe what each teaches.
- Don't give medical, psychiatric or crisis advice. Articles on grief, suffering, trauma or mortality stay general and reflective, and say plainly that persistent distress is a reason to seek professional or crisis support.
- Don't use real, named private individuals or current partisan figures in examples; use neutral everyday or workplace scenarios.
