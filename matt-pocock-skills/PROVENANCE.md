# 출처와 적용 범위

- 원본: https://github.com/mattpocock/skills
- 버전: `1.2.3` (`package.json`)
- 가져온 커밋: `d81f3a183412e71a5b1e84ca21bc1a35eea03a60`
- 라이선스: MIT (`LICENSE`)

원본의 배포 대상인 `skills/engineering/`과 `skills/productivity/`에서 스킬 27개를 가져온 뒤, 사용자의 요청에 따라 외부 Git·이슈 트래커·웹 조사 흐름을 중심으로 한 10개를 제외했습니다: `ask-matt`, `implement-spec`, `pr`, `research`, `setup-matt-pocock-skills`, `to-spec`, `to-tickets`, `triage`, `wayfinder`, `wizard`. `misc/`, `in-progress/`, `deprecated/`는 원본의 배포 대상이 아니어서 처음부터 포함하지 않았습니다.

Pi의 스킬 디렉터리에 바로 풀 수 있도록 남은 스킬 폴더를 `skills/<name>/`으로 모았습니다. `Skill tool` 호출을 언급하는 스킬에는 Pi에서 해당 스킬의 `SKILL.md`를 읽도록 안내하는 한 줄을 추가했습니다. `code-review`는 외부 이슈 트래커 대신 로컬 명세를 사용하도록, `improve-codebase-architecture`는 CDN 없이 HTML을 만들도록, `prototype`과 `teach`는 로컬 자료를 우선하도록 조정했습니다. 다른 보조 파일은 보존했습니다.
