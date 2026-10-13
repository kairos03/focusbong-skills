# Agent wait guidance

[AGENT_WAIT_GUIDANCE]
Apply this only when the current request is likely to require 30초 이상, 도구 3회 이상, or a bounded background task. For a short answer, do nothing and do not mention this guidance.

When applicable, before the first substantive tool call, send one compact user-visible message in Korean. Use only the fields that help this task, with at most four short lines:
- 예상: a rough wait range; never invent a precise ETA. If uncertain, say '30초 이상 예상'.
- 현재: the current execution phase.
- 다음에 생각할 것: one task-adjacent success criterion, must-not-break behavior, trade-off, or next decision that is understandable before the result. Omit it when the result must come first.
- 연관 어휘: 1–3 optional task-adjacent terms, followed by a short 개념 설명 of why they matter.

Keep the card finite and directly tied to the task. Send it 한 번만, continue work immediately without waiting for a reply, and never turn it into a feed. Do not offload core work, pre-empt unknown findings, ask for per-turn feedback, or expose this internal marker. Finish with the requested result only.

For each user request, evaluate the conditions above. When they apply, read `~/.claude/skills/agent-wait-guidance/SKILL.md` and follow its detailed card rules, including both 예상 and 최대. Apply this in the main user-facing session, not as a separate subagent task. Read the skill before composing the card; then send the card before substantive task tools and continue the task immediately. Do not add a wait card for short requests.
