# Matt Pocock 스킬: 폐쇄망 Pi 설치

`matt-pocock-skills-pi-offline-1.2.3.zip`에는 [원본](https://github.com/mattpocock/skills)의 배포 대상 스킬 27개가 들어 있습니다. Windows와 Linux에서 같은 ZIP을 사용합니다. 스킬 설치와 사용에 Python·npm 패키지는 필요하지 않습니다.

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

압축을 풀면 `~/.pi/agent/skills/ask-matt/SKILL.md`처럼 스킬 폴더가 바로 놓입니다. Pi가 실행 중이면 `/reload`하거나 다시 시작합니다. `/skill:ask-matt`로 사용할 스킬을 안내받거나 `/skill:tdd`처럼 원하는 스킬을 직접 호출하세요. 프로젝트에만 설치하려면 해당 프로젝트의 `.pi/skills`에 압축을 풉니다.

## 폐쇄망에서의 범위

- 스킬 문서는 로컬에서 읽을 수 있습니다. `setup-matt-pocock-skills`를 실행할 때 이슈 트래커로 **local files**를 선택하면 이슈 관련 흐름을 로컬 파일로 운영할 수 있습니다.
- GitHub·GitLab·Linear 이슈 연동, 웹 자료 조사, PR 게시 등 외부 서비스 작업은 해당 서비스에 접속할 수 있어야 합니다.
- `code-review`, `implement-spec`, `wayfinder` 등 서브에이전트 호출을 명시한 흐름은 Pi에 서브에이전트 기능을 제공하는 확장이 있어야 원문 절차대로 실행됩니다.
- `wizard`는 Bash 스크립트를 생성합니다. Windows에서 생성된 스크립트를 실행하려면 Bash 환경이 필요합니다.

원본 커밋과 변경 사항은 [PROVENANCE.md](PROVENANCE.md)에 기록했습니다. MIT 라이선스는 ZIP의 `MATT-POCOCK-LICENSE.txt`에 들어 있습니다.
