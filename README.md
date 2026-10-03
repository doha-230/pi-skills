# Pi 스킬 모음

폐쇄망에서 사용하는 Pi 코딩 에이전트용 스킬을 보관합니다. 이 저장소를 폐쇄망으로 옮긴 뒤 필요한 스킬 폴더를 Pi의 스킬 디렉터리에 복사해 사용하세요.

## 포함된 스킬

| 스킬 | 용도 | 원본 |
| --- | --- | --- |
| [humanize-korean](humanize-korean/SKILL.md) | 한국어 AI 초안의 번역투와 기계적인 표현을 진단하고 윤문 | [doha-230/im-not-ai](https://github.com/doha-230/im-not-ai) |
| [kordoc](kordoc/SKILL.md) | 폐쇄망 문서 변환·HWPX 작성용 Pi 스킬 | [chrisryugj/kordoc](https://github.com/chrisryugj/kordoc) |
| [ponytail](ponytail/skills/ponytail/SKILL.md) | 코딩 작업에서 불필요한 구현을 줄이는 Pi 확장과 6개 스킬 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |
| [matt-pocock-skills](matt-pocock-skills/INSTALL.md) | 외부 Git·웹 연동 흐름을 제외한 설계·구현·검토 스킬 17개 | [mattpocock/skills](https://github.com/mattpocock/skills) |

`humanize-korean`은 원본 저장소의 `2024ce14e4e025e53d991f296e1d35f48e328b38` 커밋에서 가져왔습니다. 스킬, 스크립트, 참고 문서와 MIT 라이선스를 함께 보관합니다. 설치 방법은 [INSTALL.txt](INSTALL.txt)를 참고하세요.

스킬의 Python 스크립트는 표준 라이브러리만 사용합니다. 윤문에는 Pi에 설정된 모델이 필요하며, 선택적 `local_runner.py`를 실행할 때만 지정한 OpenAI 호환 서버로 요청을 보냅니다.

`kordoc`은 [Windows·Linux x64 공용 오프라인 ZIP](dist/kordoc-pi-offline-4.18.8-win-linux-x64.zip)으로 설치합니다. Python 3.12 실행기가 운영체제에 맞는 동봉 Node.js를 호출합니다. 설치 방법과 지원 범위는 [kordoc/INSTALL.md](kordoc/INSTALL.md)에 있습니다.

`ponytail`은 [Windows·Linux 공용 오프라인 ZIP](dist/ponytail-pi-offline-4.10.3.zip)으로 설치합니다. Pi 전용 확장과 6개 스킬이 들어 있으며 추가 패키지 설치가 필요하지 않습니다. [설치 안내](ponytail/INSTALL.md)를 참고하세요.

`matt-pocock-skills`는 [Windows·Linux 공용 오프라인 ZIP](dist/matt-pocock-skills-pi-offline-1.2.3.zip)을 Pi의 스킬 폴더에 풀면 됩니다. 제외한 스킬과 로컬 실행 범위는 [설치 안내](matt-pocock-skills/INSTALL.md)에 정리했습니다.
