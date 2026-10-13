# Codex CLI 설치 및 스킬 적용

아래 명령은 macOS·Linux·WSL의 셸 기준입니다. 네이티브 Windows 사용자는 [공식 설치 안내](https://developers.openai.com/codex/cli)를 참고하세요.

## 1. Codex CLI 설치

Node.js와 npm이 준비되어 있다면:

```bash
npm install -g @openai/codex
codex --version
```

또는 macOS에서 Homebrew로 설치합니다. 두 방법을 중복 실행하지 마세요.

```bash
brew install --cask codex
codex --version
```

작업할 프로젝트에서 `codex`를 실행하고, 처음 표시되는 로그인 절차를 직접 완료하세요. 이 저장소에는 계정·API 키가 필요하지 않으며 인증정보를 저장하지 않습니다. CLI 이용에는 별도의 계정과 이용 조건이 적용됩니다.

## 2. 저장소 다운로드

```bash
git clone https://github.com/kairos03/focusbong-skills.git
cd focusbong-skills
```

이미 받았다면 해당 폴더에서 `git pull --ff-only`로 업데이트합니다.

## 3. 스킬 설치

Codex의 사용자 범위 스킬 위치는 `~/.agents/skills/`입니다. **아래 명령은 이 저장소 루트에서 실행**하세요. 기존 동명 스킬이 있으면 덮어쓰지 않고 중단합니다.

```bash
(
  set -eu
  dest="$HOME/.agents/skills/agent-wait-guidance"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    printf '이미 설치된 경로입니다: %s
' "$dest"
    exit 1
  fi
  mkdir -p "$HOME/.agents/skills"
  cp -R skills/agent-wait-guidance "$dest"
  test -f "$dest/SKILL.md"
  cmp skills/agent-wait-guidance/SKILL.md "$dest/SKILL.md"
)
```

특정 프로젝트에만 설치하려면, 대상 프로젝트 루트에서 `.agents/skills/agent-wait-guidance/`에 같은 스킬 폴더를 복사하세요. 사용자 범위와 프로젝트 범위에 같은 이름을 중복 설치하지 마세요.

## 4. 확인 및 직접 호출

작업 프로젝트에서 새 Codex 세션을 열고 `/skills`에 `agent-wait-guidance`가 표시되는지 확인합니다. 변경이 보이지 않으면 Codex를 다시 시작하세요.

Codex 입력창에 다음과 같이 **실제로 필요한 작업**과 함께 호출합니다.

```text
$agent-wait-guidance [AGENT_WAIT_GUIDANCE] 이 프로젝트의 테스트를 실행하고 실패 원인을 조사해줘.
```

짧은 질문에는 안내 카드가 나오지 않는 것이 정상입니다. 긴 작업에서는 한 번만 한국어로 안내하고 곧바로 작업을 이어가야 합니다.

## 5. 매 작업에 자동으로 판단하게 하기

스킬 설치만으로 메시지마다 훅이 주입되지는 않습니다. [설정 예시](../templates/codex-AGENTS.md)의 내용을 대상 프로젝트의 `AGENTS.md`에 **추가**하세요. 기존 파일을 덮어쓰지 마세요.

이 예시는 사용자 범위 설치 경로를 사용합니다. 프로젝트 범위로 설치했다면 예시의 스킬 경로를 `.agents/skills/agent-wait-guidance/SKILL.md`로 바꾸세요.

전역 적용을 원하면 기존 `~/.codex/AGENTS.md`에 병합할 수도 있습니다. 어느 범위를 선택하든 같은 지침을 중복 추가하지 마세요. 새 세션에서 확인하세요.

이는 프롬프트에 따른 동작이며, 모델이 반드시 카드나 정확한 ETA를 출력하도록 강제하는 실행형 훅은 아닙니다.

## 6. 업데이트·제거

업데이트 전 설치한 `SKILL.md`와 새 파일을 비교하세요. 개인 수정이 있다면 먼저 백업하고 병합합니다. 검토 후 파일을 교체하고 새 세션에서 확인하세요.

제거할 때는 설치한 `agent-wait-guidance` 폴더만 삭제하고 `AGENTS.md`에 추가했던 안내 블록도 제거합니다. 다른 스킬이나 기존 지침은 보존하세요.

## 공식 문서

- [CLI 설치](https://developers.openai.com/codex/cli)
- [스킬 경로 및 호출](https://developers.openai.com/codex/skills)
- [AGENTS.md 적용 범위](https://developers.openai.com/codex/guides/agents-md)
