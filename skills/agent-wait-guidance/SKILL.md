---
name: agent-wait-guidance
description: Use when [AGENT_WAIT_GUIDANCE] appears. Show wait card.
version: 1.0.0
author: Ori
license: MIT
metadata:
  hermes:
    tags: [focus, wait-state, productivity]
---

# Agent wait guidance

## Purpose

Preserve the user's task context during meaningful agent wait time. The card is not filler or a productivity feed. It should reduce uncertainty and make the eventual result or next decision easier to understand.

## When to Use

Show a card only when the request is likely to take at least 30 seconds, require three or more tool calls, or start a bounded background task. For short answers, do not mention this guidance.

## Card timing

Send exactly one compact Korean card before the first substantive tool call, then continue immediately. Never wait for the user to answer it. If the user replies mid-turn, consume that reply at the next safe checkpoint.

## Card contents

Use only the fields that are useful for the current task, with at most four short lines:

1. `예상 · 최대` (both mandatory): Always display the expected wait range and a conservative estimated upper bound together on the first line, e.g. `예상: 2~5분 · 최대: 10분`. Neither label may be omitted. The maximum estimate must be at least the range's upper end; it is not a guaranteed deadline. Never fabricate precision or an unsupported upper bound. When uncertain, display `예상: 30초 이상 · 최대: 산정 불가`.
2. `현재`: Name the current execution phase in plain language.
3. `다음에 생각할 것`: Give one success criterion, must-not-break behavior, trade-off, or next decision that is understandable before the result exists. Omit this field when the result must come first, especially in open-ended research.
4. `연관 어휘`: Give one to three optional, task-adjacent terms. Add one short `개념 설명` showing why they matter.

Prefer all four when each adds value. Omit rather than pad. The side concept must be optional and unnecessary for receiving the main result.

## Example

```text
예상: 2~5분 · 최대: 10분
현재: 구현 경로와 기존 동작 확인 중
다음에 생각할 것: 이번 변경에서 절대 깨지면 안 되는 동작은 무엇인가?
연관 어휘: `점진적 전환`, `롤백 경로` — 새 동작을 적용하면서 기존 상태로 안전하게 돌아갈 수 있는 설계다.
```

## Boundaries

- One card per task; no scroll, next-card action, streak, reward, or recommendations.
- Keep every line directly tied to the current task.
- Do not offload work the agent can perform.
- Do not anticipate unknown findings or force a premature decision.
- Do not expose internal hook markers or implementation details.
- Do not ask for run IDs, per-turn feedback, behavior reports, or surveys.
- Finish with the requested result only.

## Verification

- Applied only to a genuinely long or multi-tool task
- Sent once before substantive work
- Always displayed both 예상 and 최대 on the first line, using 산정 불가 rather than fabricating an unsupported maximum
- Used rough rather than fabricated precise timing
- Continued immediately without waiting
- Included only useful thought, terms, and explanation
- Delivered and verified the primary result
