# kordoc Pi 스킬 설치

`kordoc-pi-offline-4.18.8-win-linux-x64.zip` 파일 하나에 Windows x64와 Linux x64용 실행 파일, kordoc 4.18.8, PDF 텍스트 추출 의존성, Pi 스킬이 들어 있습니다. Python 3.12가 필요합니다. 시스템 Node.js나 npm, 인터넷 연결은 필요하지 않습니다.

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.pi\agent\skills" | Out-Null
Expand-Archive .\kordoc-pi-offline-4.18.8-win-linux-x64.zip -DestinationPath "$HOME\.pi\agent\skills" -Force
py -3.12 "$HOME\.pi\agent\skills\kordoc\scripts\kordoc.py" --version
```

## Linux

```sh
mkdir -p "$HOME/.pi/agent/skills"
python3.12 -m zipfile -e kordoc-pi-offline-4.18.8-win-linux-x64.zip "$HOME/.pi/agent/skills"
python3.12 "$HOME/.pi/agent/skills/kordoc/scripts/kordoc.py" --version
```

Pi가 이미 실행 중이면 `/reload`하거나 다시 시작합니다. 프로젝트 전용으로 설치하려면 사용자 스킬 디렉터리 대신 해당 프로젝트의 `.pi/skills`에 압축을 풉니다.

## 사용

```text
/skill:kordoc 문서.hwpx를 Markdown으로 변환해줘
```

동봉된 Python 실행기를 직접 사용할 수도 있습니다. 예를 들어 `python3.12 <설치 경로>/kordoc/scripts/kordoc.py "문서.hwpx" -o "결과.md"`입니다.

이 번들은 HWP/HWPX/HWPML, DOCX, XLS/XLSX, PPTX와 텍스트층 PDF의 읽기, HWPX 생성·검증·서식 채우기·패치·SVG 미리보기를 위한 **경량 구성**입니다. 스캔 PDF·이미지·수식 OCR, PDF 인쇄와 PNG 렌더에 필요한 플랫폼별 네이티브 엔진·모델은 포함하지 않았습니다. Linux 실행 파일은 glibc 2.28 이상인 x64 환경을 대상으로 합니다.

PDF 텍스트 추출 때 `@napi-rs/canvas`가 없다는 경고가 표시될 수 있습니다. 이 경량 번들의 텍스트 추출은 계속 진행되며, 화면 렌더링 기능은 지원 범위에 포함되지 않습니다.

원본: https://github.com/chrisryugj/kordoc (4.18.8, d15ee77d717e0670947d80b082aa5d7fa54eb249)

라이선스: `LICENSE`, `NOTICE`, `THIRD_PARTY/`, `runtime/*/LICENSE`, 설치된 각 npm 패키지의 라이선스 파일을 참조하세요.
