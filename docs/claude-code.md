# Claude Code 설치 및 스킬 적용

여기서 Claude는 **Claude Code CLI**입니다. 웹 채팅의 스킬 설치 안내가 아닙니다. 아래 셸 명령은 macOS·Linux·WSL 기준입니다.

## 1. Claude Code 설치

macOS에서 Homebrew가 있다면:

```bash
brew install --cask claude-code
claude --version
```

Homebrew가 없다면 [공식 Quickstart](https://code.claude.com/docs/en/quickstart)의 네이티브 설치 방법을 사용하세요. 다운로드 스크립트 실행 전 출처와 내용을 검토하세요. Windows 네이티브 설치 방법도 공식 문서에 있습니다.

작업할 프로젝트에서 `claude`를 실행하고, 첫 로그인과 프로젝트 신뢰 확인을 직접 완료하세요. Claude 구독 또는 Console 계정 등 공식 지원 인증 방법이 필요합니다. 인증정보를 이 저장소에 넣지 마세요.

## 2. 저장소 다운로드

```bash
git clone https://github.com/kairos03/focusbong-skills.git
cd focusbong-skills
```

이미 받았다면 해당 폴더에서 `git pull --ff-only`로 업데이트합니다.

## 3. 스킬 설치

Claude Code의 사용자 범위 스킬 위치는 `~/.claude/skills/`입니다. **이 저장소 루트에서 실행**하세요. 동명 스킬이 있으면 덮어쓰지 않고 중단합니다.

```bash
(
  set -eu
  dest="$HOME/.claude/skills/agent-wait-guidance"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    printf '이미 설치된 경로입니다: %s
' "$dest"
    exit 1
  fi
  mkdir -p "$HOME/.claude/skills"
  cp -R skills/agent-wait-guidance "$dest"
  test -f "$dest/SKILL.md"
  cmp skills/agent-wait-guidance/SKILL.md "$dest/SKILL.md"
)
```

특정 프로젝트에만 적용하려면 대상 프로젝트의 `.claude/skills/agent-wait-guidance/`에 같은 스킬 폴더를 복사하세요. 사용자 범위와 프로젝트 범위에 중복 설치할 필요는 없습니다.

## 4. 확인 및 직접 호출

대상 프로젝트에서 새 Claude Code 세션을 열고 `/` 입력 후 `agent-wait-guidance`가 표시되는지 확인하세요. 다음과 같이 작업과 함께 호출합니다.

```text
/agent-wait-guidance [AGENT_WAIT_GUIDANCE] 이 프로젝트의 테스트를 실행하고 실패 원인을 조사해줘.
```

단순 질문에서는 카드를 생략하고, 긴 작업에서는 예상·최대시간을 포함한 한국어 안내를 한 번 출력한 뒤 바로 작업해야 합니다. 카드만 내고 멈추면 올바른 동작이 아닙니다.

## 5. 매 작업에 자동으로 판단하게 하기

[설정 예시](../templates/claude-CLAUDE.md)를 대상 프로젝트의 `CLAUDE.md`에 **추가**하세요. 기존 파일을 덮어쓰지 마세요. 이 예시는 매 요청을 평가하고 필요한 작업에서 원문 스킬을 읽도록 연결합니다.

사용자 범위 설치 경로가 예시에 들어 있습니다. 프로젝트 범위 설치라면 `.claude/skills/agent-wait-guidance/SKILL.md`로 바꾸세요.

모든 프로젝트에서 적용하려면 기존 `~/.claude/CLAUDE.md`에 병합할 수도 있습니다. 프로젝트·전역 지침에 동일 블록을 중복 추가하지 마세요. 새 세션에서 동작을 확인하세요.

**이 저장소의 훅 문구는 Claude Code의 실행형 `UserPromptSubmit` 이벤트 훅이 아닙니다.** `settings.json`에 이벤트 훅을 등록하거나 명령을 실행하지 않습니다. 안내 타이밍과 내용은 모델의 지침 준수에 의존합니다.

## 6. 업데이트·제거

새 버전으로 업데이트하기 전 기존 설치 파일을 비교하고 개인 수정은 백업·병합하세요. 교체 후 새 세션에서 다시 확인합니다.

제거할 때는 설치한 `agent-wait-guidance` 폴더와 `CLAUDE.md`에 추가한 안내 블록만 제거합니다. 다른 설정과 스킬은 보존하세요.

## 공식 문서

- [설치 및 첫 로그인](https://code.claude.com/docs/en/quickstart)
- [스킬 설치 위치 및 호출](https://code.claude.com/docs/en/skills)
- [CLAUDE.md 적용 범위](https://code.claude.com/docs/en/memory)
