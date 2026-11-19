---
id: wg:decision-theory
type: Field
title: Decision theory
aliases: [theory of rational choice under uncertainty, normative decision theory, descriptive decision theory]
domain: judgment-and-decisions
summary: >-
  The study, shared by philosophy, economics and psychology, of how beliefs and desires should combine into
  choices when outcomes are uncertain (normative decision theory) and of how people actually choose (descriptive
  decision theory); it can check that a choice hangs together, but it cannot say what is worth wanting.
level: intermediate
evidenceStatus: mixed
broader: [wg:philosophy, wg:economics]
related: [wg:satisficing, wg:major-life-decision, wg:reversible-and-irreversible-decisions, wg:big-decisions-opting-converting-drifting, wg:moral-algebra, wg:deliberation, wg:practical-wisdom, wg:regret, wg:weakness-of-will, wg:fast-and-frugal-heuristics, wg:kill-criteria]
requires: []
relations:
  - {predicate: appliedIn, object: wg:decisions-under-uncertainty, source: s1, confidence: high}
  - {predicate: challengedBy, object: wg:allais-paradox, source: s2, confidence: high}
  - {predicate: challengedBy, object: wg:ellsberg-paradox, source: s2, confidence: high}
  - {predicate: contrastsWith, object: wg:bounded-rationality, source: s4, confidence: high}
  - {predicate: supportedBy, object: wg:prospect-theory-replication-study, source: s3, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Decision Theory"
    publisher: Stanford Encyclopedia of Philosophy (H. Orri Stefánsson; earlier versions with Katie Steele; first published 2015, substantive revision 2025)
    url: https://plato.stanford.edu/ENTRiES/decision-theory/
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s2
    title: "Descriptive Decision Theory"
    publisher: Stanford Encyclopedia of Philosophy (Jake Chandler; first published 2017)
    url: https://plato.stanford.edu/entries/decision-theory-descriptive/
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s3
    title: "Replicating patterns of prospect theory for decision under risk"
    publisher: Nature Human Behaviour, 4(6), 622–633 (Ruggeri et al., 2020; doi:10.1038/s41562-020-0886-x), Oxford University Research Archive record
    url: https://ora.ox.ac.uk/objects/uuid:9da308a9-010d-4e44-9943-9cbd989e5e01
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Bounded Rationality"
    publisher: Stanford Encyclopedia of Philosophy (Gregory Wheeler; first published 2018, substantive revision 2024)
    url: https://plato.stanford.edu/ENTRIES/bounded-rationality/
    type: scholarly-encyclopedia
    accessed: 2026-11-19
  - id: s5
    title: "How (far) can rationality be naturalized?"
    publisher: Synthese, 187, 243–268 (Gigerenzer & Sturm, 2012), CORE open-access copy
    url: https://core.ac.uk/download/210693851.pdf
    type: peer-reviewed
    accessed: 2026-11-19
created: 2026-11-19
---

# Decision theory

Decision theory studies the reasoning behind choices. Its **normative** branch asks what standards a reasonable agent's preferences, beliefs and desires should meet, and how they should combine into a choice when outcomes are uncertain.[^s1] Its **descriptive** branch charts and explains the regular patterns in what people actually choose.[^s2] The central normative idea is expected utility: rank each option by how much you value its possible outcomes, weighted by how likely you think they are.[^s1][^s2] For anyone trying to decide wisely, the field gives a clear picture of what a coherent choice looks like. It is just as clear about what such a picture leaves out.[^s1][^s4]

## Origin

The modern theory grew from attempts to measure belief and desire through choice. Frank Ramsey suggested in 1926 that gambles could reveal how strongly someone prefers one outcome to another.[^s1] John von Neumann and Oskar Morgenstern then showed that preferences over lotteries can be represented as maximizing expected utility if they satisfy a few axioms, such as completeness, transitivity, continuity and independence.[^s1] Leonard Savage's 1954 theory went further. Working from preferences over acts alone, it derived both a probability function for beliefs and a utility function for desires.[^s1][^s2] Richard Jeffrey later offered a version in which acts, states and outcomes are all propositions.[^s1]

Challenges came quickly. Maurice Allais described choices that many thoughtful people make but that violate the independence axiom. Daniel Ellsberg showed that people prefer known odds to unknown ones, even where expected utility says this should make no difference.[^s2] Herbert Simon argued in the 1950s that real agents cannot be "globally" rational. Deliberation has costs, and a theory of choice should count them.[^s4] Daniel Kahneman and Amos Tversky's prospect theory (1979), and its 1992 cumulative version, became the leading descriptive alternative. In it, outcomes count as gains or losses from a reference point, and probabilities are weighted rather than taken at face value.[^s2][^s3]

## Why it matters

Decision theory turns vague hopes of choosing well into checkable questions. Do I prefer A to B and B to C, but C to A? Am I avoiding an option only because its odds are unknown? Would I pay to avoid information that costs nothing?[^s1][^s2] Its treatment of choices over time speaks directly to self-control. Should Ulysses trust his later self, or have himself tied to the mast because he expects to give in? The entry's own answer is the "sophisticated" one: plan around the choices you predict you will actually make, not the ones you wish you would.[^s1]

The field is also frank about its limits. Its own authors note that expected utility theory lacks the "conceptual resources to describe the reasons" behind a person's preferences.[^s1] It says how to be consistent given what you value and believe. It does not say what is worth valuing, or how far to trust your evidence. In the entry's example, a climber choosing whether to try a summit must judge whether general weather statistics apply to her particular day.[^s1] Weighing what truly matters and judging how far evidence applies are jobs for the practical judgment that wisdom traditions and wisdom research describe.[^s1]

## What the field offers in practice

- **Lay out the decision.** List the options, the states of the world that matter and the outcomes, so that beliefs and values can be examined separately.[^s1]
- **Test patterns on reflection.** Savage changed his own Allais-style choices after thinking them through. In early studies, people often corrected intransitive choices on reflection, but Allais and Ellsberg patterns tended to persist.[^s2]
- **Match the tool to the world.** Optimizing models work best in "small worlds," where every relevant option and probability is known. Under real uncertainty, with little data, simple heuristics can predict as well or better because they do not overfit.[^s5][^s4]
- **Plan for your future self.** When you expect your preferences to drift, commitments and safeguards are often wiser than counting on willpower.[^s1]

At work, a team picking a supplier might map scenarios and estimate their likelihood. Then it should ask which risks it simply cannot estimate. That is where a reversible trial, a backup plan or a clear exit rule may beat a precise-looking spreadsheet.[^s1][^s5]

## Evidence and limits

The descriptive findings are among the best replicated in behavioural science. A 2020 replication of the original prospect-theory problems tested 4,098 people in 19 countries and 13 languages. It reproduced the original pattern on 94% of items, with smaller effects, and supported 12 of 13 theoretical contrasts. It also found variation between countries.[^s3] The normative side is a matter of argument, not experiment, and remains contested. Philosophers dispute whether completeness and independence are true requirements of rationality, and how to choose under vague probabilities, catastrophic risk or unawareness of unknown possibilities.[^s1] There is also a running debate over whether departures from expected utility are errors. The heuristics-and-biases tradition generally treats them as errors. Gigerenzer's ecological-rationality programme argues that many are reasonable responses to costly thinking and uncertain environments.[^s4][^s5] The evidence status is therefore **mixed**: the descriptive regularities hold up well, while the claim that one formal standard defines wise choice does not.[^s1][^s3][^s4]

## Connections

Decision theory is **applied in decisions under uncertainty**, the setting its normative branch was built for.[^s1] It is **challenged by the Allais and Ellsberg paradoxes**, choices that many people make on reflection and that violate the theory's axioms.[^s2] It **contrasts with bounded rationality**, Simon's view that real agents must count the cost of thinking. Satisficing and fast-and-frugal heuristics grew out of that view.[^s4][^s5] Its descriptive branch is **supported by the 2020 multinational replication of prospect theory**.[^s3] Regret theory offers one explanation of Allais-style choices, which links the field to **regret**. Its treatment of Ulysses and the sirens bears on **weakness of will**.[^s1][^s2] Decision theory gives formal grounding to everyday guides such as **reversible and irreversible decisions**, **kill criteria** and **moral algebra**. It leaves to **practical wisdom** and **deliberation** the questions of what is worth wanting and how far to trust the evidence.[^s1][^s4]

## Sources

[^s1]: Stefánsson, H. O. (earlier versions with K. Steele). "Decision Theory." *Stanford Encyclopedia of Philosophy* (first published 2015; substantive revision 2025), §§1–3, 4.2, 5–7. https://plato.stanford.edu/ENTRiES/decision-theory/ (accessed 2026-11-19)
[^s2]: Chandler, J. "Descriptive Decision Theory." *Stanford Encyclopedia of Philosophy* (first published 2017), §§1–3, 5. https://plato.stanford.edu/entries/decision-theory-descriptive/ (accessed 2026-11-19)
[^s3]: Ruggeri, K., et al. (2020). "Replicating patterns of prospect theory for decision under risk." *Nature Human Behaviour*, 4(6), 622–633. https://ora.ox.ac.uk/objects/uuid:9da308a9-010d-4e44-9943-9cbd989e5e01 (accessed 2026-11-19)
[^s4]: Wheeler, G. "Bounded Rationality." *Stanford Encyclopedia of Philosophy* (first published 2018; substantive revision 2024), §§1–2, 5. https://plato.stanford.edu/ENTRIES/bounded-rationality/ (accessed 2026-11-19)
[^s5]: Gigerenzer, G., & Sturm, T. (2012). "How (far) can rationality be naturalized?" *Synthese*, 187, 243–268, pp. 255–264. https://core.ac.uk/download/210693851.pdf (accessed 2026-11-19)
