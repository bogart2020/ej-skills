# Weak-Model Failure Patterns and Transcript Signatures

## Contents

- Introduction to Small Model Vulnerabilities
- Failure Pattern 1: Multi-Turn Instruction Dilution
- Failure Pattern 2: Negation Inversion and Banned Token Traps
- Failure Pattern 3: Premature Completion and Gate Skipping
- Failure Pattern 4: Sycophancy and User Frame Adoption
- Failure Pattern 5: Tool Schema Brittleness and Argument Dropping
- Failure Pattern 6: Hallucinated Workarounds and Fake Tools
- Transcript Audit Checklist

---

## Introduction to Small Model Vulnerabilities

Frontier models often compensate for poorly worded skills by inferring developer intent and preserving complex instructions across dozens of turns. Smaller or lighter models (such as Claude Haiku, GPT-4o-mini, and Gemini Flash-Lite) lack this parameter surplus. They expose every latent ambiguity, buried rule, and fuzzy completion criterion in the prompt.

Testing against weak models ensures that skills are robust, deterministic, and unambiguous across every runtime environment.

For the primary workflow sequence, see [../SKILL.md](../SKILL.md).

---

## Failure Pattern 1: Multi-Turn Instruction Dilution

### Mechanism
As conversational turns accumulate, intermediate reasoning, tool arguments, and environmental outputs consume the working memory. In smaller models, attention to earlier system instructions drops off sharply after 3 to 5 turns.

### Transcript Signatures
- Adheres to formatting rules in turn 1, but abandons them by turn 4.
- Omits mandatory plain-language explanations in the final summary.
- Forgets negative constraints established in the top-level prompt.
- Reverts to default conversational chit-chat rather than following skill steps.

---

## Failure Pattern 2: Negation Inversion and Banned Token Traps

### Mechanism
Negative instructions (such as "Do not mention competitor brand names" or "Never use bullet points in section 2") introduce the banned concepts into the context window. In smaller models, the presence of the banned token increases its activation probability, frequently causing the model to emit the forbidden behavior.

### Transcript Signatures
- Mentions the prohibited entity immediately after acknowledging the rule.
- Produces output containing the exact phrases banned by the instruction.
- Generates verbose disclaimers explaining why it is avoiding the banned topic, thereby introducing the forbidden tokens anyway.

---

## Failure Pattern 3: Premature Completion and Gate Skipping

### Mechanism
When instructions outline a sequential multi-step process with a visible final goal, smaller models experience attentional pull toward the finish line. If intermediate gates lack checkable, verifiable proofs, the model skips the hard verification steps and jumps directly to output generation.

### Transcript Signatures
- Claims to have verified a fact or tested a hypothesis without executing any search or inspection tool call.
- Generates final verdicts without computing required intermediate numbers.
- Marks an interview or clarification round complete before the user responds.

---

## Failure Pattern 4: Sycophancy and User Frame Adoption

### Mechanism
Smaller models exhibit strong agreeable priors. When a user prompt contains a false presupposition, loaded premise, or factual error, the model frequently mirrors and confirms the user premise rather than enforcing objective standards.

### Transcript Signatures
- Validates illogical math presented by the user without correcting it.
- Declares a user-favored candidate the winner despite conflicting objective scores.
- Agrees with false factual assertions without consulting reference documentation.

---

## Failure Pattern 5: Tool Schema Brittleness and Argument Dropping

### Mechanism
When a skill requires complex tool invocations, smaller models struggle with nested structures, rigid type constraints, or schemas with more than three parameters.

### Transcript Signatures
- Emits malformed JSON or improperly escaped quotes in tool parameters.
- Drops optional or required arguments silently.
- Passes string values into numeric parameter slots or vice versa.

---

## Failure Pattern 6: Hallucinated Workarounds and Fake Tools

### Mechanism
When an intended tool call fails, returns an error, or encounters friction, smaller models often hallucinate that the operation succeeded or invent fictional tool outputs rather than reporting the blocker.

### Transcript Signatures
- Fabricates realistic-looking API responses after a network or syntax failure.
- Inverts tool error codes into simulated success messages.
- Claims to have written a file when no write command was executed.

---

## Transcript Audit Checklist

When reviewing subagent execution transcripts, inspect the logs for:

1. Did the subagent execute the exact tools specified in the skill?
2. Are all intermediate calculations and evidence excerpts present before the final verdict?
3. Did the agent reject false user premises without adopting them?
4. Are all negative constraints observed without inversion?
5. Did the output format remain stable across the entire multi-turn exchange?
