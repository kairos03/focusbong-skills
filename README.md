# focusbong-skills

AI 에이전트가 일하는 동안, 사용자의 작업 맥락이 끊기지 않도록 돕는 스킬 모음입니다.

첫 번째 스킬 **agent-wait-guidance**는 긴 작업을 시작할 때 예상·최대 대기시간, 현재 단계, 다음에 생각할 것을 짧게 알려줍니다. 안내 뒤에는 답변을 기다리지 않고 바로 작업을 이어갑니다.

## 안내 예시

```text
예상: 2~5분 · 최대: 10분
현재: 구현 경로와 기존 동작 확인 중
다음에 생각할 것: 이번 변경에서 절대 깨지면 안 되는 동작은 무엇인가?
연관 어휘: 점진적 전환, 롤백 경로 — 새 동작을 적용하면서 기존 상태로 안전하게 돌아갈 수 있는 설계다.
```

- 30초 이상 예상되거나, 도구 호출이 3회 이상 필요하거나, 종료가 있는 백그라운드 작업일 때만 안내합니다.
- 작업당 한 번, 최대 네 줄로 안내합니다. 짧은 질문에는 붙이지 않습니다.
- 예상·최대시간은 추정치이지 완료 보장이 아닙니다. 근거가 없으면 `최대: 산정 불가`로 표시합니다.
- 다음 생각거리는 결과가 나오기 전에도 이해할 수 있는 성공 기준·보존해야 할 동작·선택사항입니다. 에이전트의 일을 사용자에게 떠넘기지 않습니다.

## 설치

- [Codex CLI 설치 및 스킬 적용](docs/codex.md)
- [Claude Code 설치 및 스킬 적용](docs/claude-code.md)

두 가이드는 CLI 자체 설치, 스킬 설치, 직접 호출, 자동 적용 설정, 제거 방법을 포함합니다. 셸 명령은 macOS·Linux·WSL 기준입니다.

## 원문 구성

- [`prompts/agent-wait-guidance.md`](prompts/agent-wait-guidance.md): 메시지에 붙던 훅 문구 원문
- [`skills/agent-wait-guidance/SKILL.md`](skills/agent-wait-guidance/SKILL.md): 세부 규칙을 담은 스킬 원문
- [`templates/codex-AGENTS.md`](templates/codex-AGENTS.md): Codex 프로젝트 설정에 덧붙일 예시
- [`templates/claude-CLAUDE.md`](templates/claude-CLAUDE.md): Claude Code 프로젝트 설정에 덧붙일 예시

**훅과 스킬 원문은 수정하지 않았습니다.** 훅에는 최대시간 규칙이 없고, 스킬에는 예상·최대시간을 함께 표시하도록 명시되어 있습니다. 설치 가이드는 원문 스킬의 상세 규칙을 따르도록 연결합니다.

여기서 “훅”은 모델에 넣는 안내 프롬프트를 뜻합니다. 실행형 Claude Code 이벤트 훅이나 Codex 이벤트 플러그인은 아닙니다. 스킬을 복사하는 것만으로 매 메시지에 훅이 자동 주입되지는 않습니다. 직접 호출하거나, 가이드대로 프로젝트 지침에 연결해야 합니다.

이 스킬은 모델의 판단에 의존합니다. 실제 소요시간을 측정하는 타이머나 표시를 강제하는 UI가 아닙니다. 이 배포 초안에서 원문 보존·설치 경로·파일 형식은 확인했지만, 두 CLI의 실제 작업 응답을 종단간 테스트하지는 않았습니다.

## 검증

Python 3으로 패키지의 필수 파일·스킬 메타데이터·Markdown 링크·설치 복사를 확인할 수 있습니다.

```bash
python3 scripts/verify.py
```

## 공식 문서

- [Codex CLI](https://developers.openai.com/codex/cli)
- [Codex Skills](https://developers.openai.com/codex/skills)
- [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Claude Code Memory](https://code.claude.com/docs/en/memory)

## License

MIT. 스킬 원문의 작성자 표기 `Ori`를 유지합니다.
