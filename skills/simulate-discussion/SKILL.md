---
name: simulate-discussion
description: Simulate a discussion or debate about a decision, plan or topic through distinct expert and stakeholder viewpoints, then show agreements, real disagreements and what evidence would settle them. Invoke by name.
disable-model-invocation: true
---

# Simulate a discussion

This skill does one thing: it exposes the tradeoffs in a decision by letting distinct simulated viewpoints argue it out. It is a reasoning aid, not evidence.

1. **Name the decision** or topic, and what the user needs to leave with.
2. **Choose 3 to 6 participants** whose expertise, incentives or evidence standards differ. Useful kinds: domain expert, practitioner, user or customer, skeptic or risk owner, decision-maker, policy or compliance voice, contrarian. Merge any two who would make the same argument.
3. **Introduce each by role,** with one line on why they belong. Never present a real person's invented words as a quote.
4. **Let them argue.** Each gives specific arguments, concerns and a likely recommendation, and answers the strongest opposing point rather than a weak version of it.
5. **Ground the facts.** Separate evidence from assumption. Do not invent numbers, citations or events. Inspect sources when the user wants current or sourced claims, and say when information is missing.
6. **Close** with agreements, the disagreements that remain and what is really at stake in each, a recommendation if one was asked for, and the evidence that would change it. Do not force consensus.

Default shape, adapted when the user asks for a debate, meeting, review board or transcript:

```markdown
Simulated participants:
- <Role>: <why this perspective matters>

Discussion:
- <Role>: <argument>
- <Role>: <response or counterpoint>

Key disagreements:
- <Disagreement>: <what is at stake>

Synthesis:
<conclusion, implications, and what would change the answer>
```

State at the top that the discussion is simulated. Agreement among simulated roles is structured judgment, not independent validation.
