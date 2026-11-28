---
name: research
description: Use when an engineering question needs an answer from primary sources - how an API or library behaves, whether an installed version supports something, what a standard says, or which option fits. Returns cited findings. Not for documenting the project's own implemented code.
---

# Research a decision

This skill does one thing: it answers an engineering question from sources that own the answer, and says how confident the answer is.

1. **State the question,** its scope and what evidence would change the decision. Check: you can say what a complete answer looks like.
2. **Check the local facts first.** Installed versions, lock files, configuration and the code that uses the thing in question.
3. **Find the owning source for each consequential claim.** Read [source ranking](references/sources.md) when sources conflict or the obvious ones are secondary.
4. **Open the sources.** Check dates and versions against the installed ones. Trace commentary back to the evidence it cites. A popular repository or a large install count says nothing about quality for this task.
5. **Compare options against the user's constraints.** Keep facts, inferences, unknowns and recommendations separate.
6. **Answer** with [the answer template](assets/answer.md). Cite the page or pinned source for each consequential claim. Say where sources disagree or access was missing.

Write a file only when the user asked for one or it is an agreed deliverable. Delegating to subagents is optional, not a requirement.
