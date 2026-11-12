"""End-to-end tests for scripts/kg.py against a throwaway tree of fixture articles.

Fixtures use example.org URLs and synthetic prose: they exercise the validator,
reasoner, SHACL shapes and exports, and are never part of the real graph.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
KG = REPO / "scripts" / "kg.py"


def body(slug: str, sections: list[str]) -> str:
    def para(i: int) -> str:
        words = " ".join(f"{slug.replace('-', '')}{i}w{j}" for j in range(150))
        return f"Synthetic fixture prose for {slug} paragraph {i}: {words}.[^s1][^s2][^s3]"
    out = [f"# {slug}", "", para(0), "", para(1), ""]
    for k, s in enumerate(sections, 2):
        out += [s, "", para(k), ""]
    out += ["## Connections", "", para(99), "", "## Sources", "",
            "[^s1]: Fixture one. https://example.org/1", "[^s2]: Fixture two. https://example.org/2",
            "[^s3]: Fixture three. https://example.org/3"]
    return "\n".join(out) + "\n"


SOURCES = """sources:
  - {id: s1, title: Fixture one, publisher: Example, url: "https://example.org/SLUG/1", type: peer-reviewed, accessed: 2026-11-02}
  - {id: s2, title: Fixture two, publisher: Example, url: "https://example.org/SLUG/2", type: practitioner-journal, accessed: 2026-11-02}
  - {id: s3, title: Fixture three, publisher: Example, url: "https://example.org/SLUG/3", type: textbook, accessed: 2026-11-02}
created: 2026-11-02
"""

ARTICLES = {
    ("science-of-wisdom", "wise-reasoning"): ("""id: wg:wise-reasoning
type: Skill
title: Wise reasoning
aliases: [wise thinking]
domain: science-of-wisdom
summary: Reasoning about a real problem with intellectual humility, attention to other viewpoints, change and uncertainty, and a search for compromise.
level: introductory
evidenceStatus: robust
broader: [wg:practical-wisdom]
related: [wg:intellectual-humility]
relations:
  - {predicate: demonstratedBy, object: wg:wise-reasoning-study, source: s1, confidence: high}
  - {predicate: introducedBy, object: wg:igor-grossmann, source: s3}
selfCheck:
  - Have I considered how the other person sees this situation?
  - What would change my mind about what is going on here?
""", ["## What good looks like", "## How to practise it"]),
    ("self-knowledge", "self-distancing"): ("""id: wg:self-distancing
type: Practice
title: Self-distancing
domain: self-knowledge
summary: Reflecting on your own situation from an outside observer's perspective, for example by using your own name or the third person.
level: introductory
evidenceStatus: mixed
broader: [wg:reflective-practices]
requires: [wg:wise-reasoning]
relations:
  - {predicate: develops, object: wg:wise-reasoning, source: s1, confidence: high}
  - {predicate: addresses, object: wg:rashness, source: s2}
  - {predicate: appliedIn, object: wg:interpersonal-conflict, source: s2}
  - {predicate: rootedIn, object: wg:stoicism, source: s3, confidence: low}
  - {predicate: confusedWith, object: wg:emotional-avoidance, source: s3, confidence: low}
steps:
  - Pause before responding to the situation that upset you.
  - Describe the situation to yourself in the third person, using your own name.
  - Ask what advice you would give a friend in exactly this position.
example:
  situation: A colleague takes credit for your work in a meeting.
  before: "I am going to call them out in front of everyone right now."
  after: "What would Sam tell a friend here? Probably to raise it privately and calmly first."
  why: Stepping outside the moment shifts attention from the sting to the outcome you actually want.
selfCheck:
  - Did I look at this as an outsider would before acting?
  - Would I give a friend the advice I am about to follow?
""", ["## How to apply it", "## Common mistakes"]),
    ("virtues-and-character", "rashness"): ("""id: wg:rashness
type: Vice
title: Rashness
domain: virtues-and-character
summary: Rushing into risk or action without due deliberation, the excess that Aristotle set against cowardice on either side of courage.
level: introductory
evidenceStatus: normative
broader: [wg:vices-of-excess]
related: [wg:impulsivity]
relations:
  - {predicate: excessOf, object: wg:courage, source: s1, confidence: high}
  - {predicate: undermines, object: wg:good-judgment, source: s1, confidence: medium}
example:
  situation: A manager hears a rumour that a key client is unhappy.
  before: "Cancel the project review and fly out tomorrow to fix it."
  after: "First I'll call the account lead and find out what the client actually said."
  why: Checking the facts first turns a bold but blind move into a bold and informed one.
selfCheck:
  - Have I gathered the facts I need before acting?
  - Is this courage, or am I just impatient?
""", ["## How to spot it", "## How to fix it"]),
    ("science-of-wisdom", "solomons-paradox"): ("""id: wg:solomons-paradox
type: Obstacle
title: Solomon's paradox
domain: science-of-wisdom
summary: The tendency to reason more wisely about other people's problems than about one's own.
level: intermediate
evidenceStatus: robust
broader: [wg:obstacles-to-wise-reasoning]
related: [wg:egocentric-bias]
requires: [wg:perspective-taking]
relations:
  - {predicate: demonstratedBy, object: wg:solomons-paradox-study, source: s1, confidence: high}
selfCheck:
  - Would I see this more clearly if it were happening to a friend?
  - Am I too close to this problem to judge it well?
""", ["## Evidence", "## How to spot it", "## How to fix it"]),
    ("wisdom-traditions", "stoicism"): ("""id: wg:stoicism
type: Tradition
title: Stoicism
domain: wisdom-traditions
summary: A Hellenistic school of philosophy holding that virtue is the only true good and that we should focus on what is within our control.
level: introductory
evidenceStatus: historical
broader: [wg:hellenistic-philosophy]
relations:
  - {predicate: introducedBy, object: wg:zeno-of-citium, source: s1, confidence: high}
  - {predicate: influencedBy, object: wg:socratic-philosophy, source: s3}
""", ["## Key teachings", "## Common misreadings"]),
}


def make_tree(tmp: Path, articles=ARTICLES) -> Path:
    for d in ("ontology", "topics", "queries"):
        shutil.copytree(REPO / d, tmp / d)
    for (dom, slug), (fm, secs) in articles.items():
        p = tmp / "articles" / dom / f"{slug}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\n{fm}{SOURCES.replace('SLUG', slug)}---\n{body(slug, secs)}")
    return tmp


def run(tmp: Path, *args: str, hashseed: str = "random") -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(KG), *args], cwd=tmp, env={"PYTHONHASHSEED": hashseed, "WG_KG_ROOT": str(tmp), "PATH": ""},
                          capture_output=True, text=True)


def test_valid_tree_builds(tmp_path):
    t = make_tree(tmp_path)
    r = run(t, "build")
    assert r.returncode == 0, r.stdout + r.stderr
    g = t / "graph"
    inferred = (g / "inferred.nt").read_text()
    ns = "https://github.com/john1hsu/wisdom-graph/"
    # inverse property materialised by the reasoner
    assert f"rashness> <{ns}ontology#addressedBy> <{ns}id/self-distancing>" in inferred
    assert f"wise-reasoning> <{ns}ontology#developedBy> <{ns}id/self-distancing>" in inferred
    assert f"stoicism> <{ns}ontology#teaches> <{ns}id/self-distancing>" in inferred
    # doctrine of the mean: excessOf types its target as a Virtue and adds the inverse
    assert f"courage> <{ns}ontology#hasExcess> <{ns}id/rashness>" in inferred
    assert f"courage> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ns}ontology#Virtue>" in inferred
    # symmetric property materialised
    assert f"emotional-avoidance> <{ns}ontology#confusedWith>" in inferred
    # range axioms type unwritten frontier nodes
    assert f"solomons-paradox-study> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ns}ontology#Study>" in inferred
    frontier = (g / "frontier.md").read_text()
    assert "`wg:igor-grossmann`" in frontier and "Person" in frontier
    assert "<< <" in (g / "edge-evidence.ttls").read_text()
    play = (g / "playbook.md").read_text()
    assert "| Before | After |" in play and "1. Pause before responding" in play and "Ask yourself:" in play
    assert "HowToStep" in (g / "triples.nt").read_text()
    idx = json.loads((g / "index.json").read_text())
    assert {x["id"] for x in idx} == {"wg:wise-reasoning", "wg:self-distancing", "wg:rashness",
                                      "wg:solomons-paradox", "wg:stoicism"}
    comp = (g / "competency.md").read_text()
    assert "wg:solomons-paradox" in comp  # obstacle with no remedy -> gap
    path = (g / "learning-path.md").read_text()
    assert path.index("Wise reasoning") < path.index("Self-distancing")
    # deterministic: rebuilding under different hash seeds (as CI and scheduled runs do) is byte-identical
    before = {p.name: p.read_text() for p in g.iterdir()}
    for seed in ("1", "2", "3", "4"):
        assert run(t, "build", hashseed=seed).returncode == 0
        assert before == {p.name: p.read_text() for p in g.iterdir()}, f"output changed with PYTHONHASHSEED={seed}"


def mutate(key, old, new):
    arts = dict(ARTICLES)
    fm, secs = arts[key]
    assert old in fm
    arts[key] = (fm.replace(old, new), secs)
    return arts


@pytest.mark.parametrize("key,old,new,expect", [
    (("self-knowledge", "self-distancing"), "type: Practice", "type: Vice", "develops expects subject"),
    (("science-of-wisdom", "wise-reasoning"), "source: s3}", "source: s9}", "unknown source"),
    (("science-of-wisdom", "wise-reasoning"), "evidenceStatus: robust", "evidenceStatus: contested", "needs a challengedBy"),
    (("self-knowledge", "self-distancing"), "  - Pause before responding to the situation that upset you.\n", "", ">= 3 steps"),
    (("virtues-and-character", "rashness"), "  - Is this courage, or am I just impatient?\n", "", ">= 2 selfCheck"),
    (("virtues-and-character", "rashness"), "after: \"First I'll call the account lead and find out what the client actually said.\"",
     "after: \"Cancel the project review and fly out tomorrow to fix it.\"", "before and after are the same"),
    (("self-knowledge", "self-distancing"), "title: Self-distancing", "title: Self-distancing\naliases: [wise thinking]",
     "collides"),
    (("science-of-wisdom", "wise-reasoning"), "introducedBy, object: wg:igor-grossmann",
     "introducedBy, object: wg:wise-reasoning-study", "contradiction"),
    (("virtues-and-character", "rashness"), "excessOf, object: wg:courage", "excessOf, object: wg:self-distancing",
     "expects object in ['Virtue']"),
])
def test_rejections(tmp_path, key, old, new, expect):
    t = make_tree(tmp_path, mutate(key, old, new))
    r = run(t, "check")
    assert r.returncode == 1 and expect in r.stdout, r.stdout


def test_tradition_sections(tmp_path):
    t = make_tree(tmp_path)
    p = t / "articles" / "wisdom-traditions" / "stoicism.md"
    p.write_text(p.read_text().replace("## Common misreadings", "## Other notes"))
    r = run(t, "check")
    assert r.returncode == 1 and "Common misreadings" in r.stdout, r.stdout


def test_virtue_needs_self_check(tmp_path):
    arts = dict(ARTICLES)
    arts[("virtues-and-character", "courage")] = ("""id: wg:courage
type: Virtue
title: Courage
domain: virtues-and-character
summary: The disposition to act rightly in the face of fear, risk or danger, lying between cowardice and rashness.
level: introductory
evidenceStatus: normative
broader: [wg:cardinal-virtues]
related: [wg:fortitude]
relations:
  - {predicate: rootedIn, object: wg:aristotelian-virtue-ethics, source: s1}
""", ["## What good looks like", "## How to practise it"])
    r = run(make_tree(tmp_path, arts), "check")
    assert r.returncode == 1 and ">= 2 selfCheck" in r.stdout, r.stdout


def test_requires_cycle(tmp_path):
    arts = mutate(("science-of-wisdom", "wise-reasoning"), "related: [wg:intellectual-humility]",
                  "related: [wg:intellectual-humility]\nrequires: [wg:self-distancing]")
    r = run(make_tree(tmp_path, arts), "check")
    assert r.returncode == 1 and "cycle in 'requires'" in r.stdout


def test_banned_source(tmp_path):
    t = make_tree(tmp_path)
    p = t / "articles" / "virtues-and-character" / "rashness.md"
    p.write_text(p.read_text().replace("https://example.org/rashness/1", "https://www.brainyquote.com/X"))
    r = run(t, "check")
    assert r.returncode == 1 and "banned domain" in r.stdout


def test_similar_and_new(tmp_path):
    t = make_tree(tmp_path)
    r = run(t, "similar", "wise thinking")
    assert r.returncode == 0 and r.stdout.splitlines()[1].split()[3] == "wg:wise-reasoning"
    r = run(t, "new", "emotions-and-equanimity", "negative-visualization", "Practice")
    assert r.returncode == 0
    text = (t / "articles" / "emotions-and-equanimity" / "negative-visualization.md").read_text()
    assert "steps:" in text and "example:" in text and "selfCheck:" in text and "## Common mistakes" in text
    r = run(t, "new", "wisdom-traditions", "daoism", "Tradition")
    assert r.returncode == 0
    assert "## Key teachings" in (t / "articles" / "wisdom-traditions" / "daoism.md").read_text()
    r = run(t, "new", "virtues-and-character", "patience", "Virtue")
    assert r.returncode == 0 and "selfCheck:" in (t / "articles" / "virtues-and-character" / "patience.md").read_text()


def test_empty_tree(tmp_path):
    t = make_tree(tmp_path, {})
    r = run(t, "build")
    assert r.returncode == 0, r.stdout
