# Matt Pocock 스킬: 폐쇄망 Pi 설치

`matt-pocock-skills-pi-offline-1.2.3.zip`에는 [원본](https://github.com/mattpocock/skills)에서 외부 Git·이슈 트래커·웹 조사 흐름을 제외한 스킬 17개가 들어 있습니다. Windows와 Linux에서 같은 ZIP을 사용합니다. 스킬 설치와 사용에 Python·npm 패키지는 필요하지 않습니다.

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.pi\agent\skills" | Out-Null
Expand-Archive .\matt-pocock-skills-pi-offline-1.2.3.zip -DestinationPath "$HOME\.pi\agent\skills" -Force
```

## Linux

```sh
mkdir -p "$HOME/.pi/agent/skills"
python3.12 -m zipfile -e matt-pocock-skills-pi-offline-1.2.3.zip "$HOME/.pi/agent/skills"
```

압축을 풀면 `~/.pi/agent/skills/tdd/SKILL.md`처럼 스킬 폴더가 바로 놓입니다. Pi가 실행 중이면 `/reload`하거나 다시 시작합니다. `/skill:tdd`처럼 원하는 스킬을 직접 호출하세요. 프로젝트에만 설치하려면 해당 프로젝트의 `.pi/skills`에 압축을 풉니다.

이전 27개짜리 ZIP을 같은 위치에 설치했다면, 압축을 새로 풀어도 제외된 폴더는 자동으로 지워지지 않습니다. 아래 10개 폴더를 기존 스킬 디렉터리에서 삭제한 다음 `/reload`하세요. 프로젝트 전용으로 설치했다면 `~/.pi/agent/skills` 대신 그 프로젝트의 `.pi/skills`에서 삭제합니다.

```text
ask-matt  implement-spec  pr  research  setup-matt-pocock-skills
to-spec  to-tickets  triage  wayfinder  wizard
```

## 포함 범위

- GitHub·GitLab·Linear 이슈 관리, PR 작성, 웹 조사, 외부 서비스 설정을 주목적으로 하는 스킬 10개를 제외했습니다.
- 로컬 `git diff`를 쓰는 `code-review`와 로컬 HTML을 만드는 `prototype`은 포함합니다. `code-review`는 로컬 명세 파일이나 사용자가 제공한 요구사항을 사용합니다.
- `improve-codebase-architecture`의 HTML 보고서는 외부 CDN 없이 로컬 CSS·SVG로 작성하도록 조정했습니다.
- 원본에서 서브에이전트를 요구한 스킬은 Pi에 해당 기능이 없으면 순차적으로 수행하도록 조정했습니다. 프로젝트별 도구가 필요한 작업은 그 프로젝트에서 사용할 수 있는 도구에 따릅니다.

원본 커밋과 변경 사항은 [PROVENANCE.md](PROVENANCE.md)에 기록했습니다. MIT 라이선스는 ZIP의 `MATT-POCOCK-LICENSE.txt`에 들어 있습니다.
