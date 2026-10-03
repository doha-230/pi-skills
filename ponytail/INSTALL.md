# Ponytail 폐쇄망 Pi 설치

`ponytail-pi-offline-4.10.3.zip`을 폐쇄망 PC로 옮깁니다. Pi 코딩 에이전트가 설치되어 있어야 합니다. 추가 npm 패키지나 Python 패키지는 필요하지 않습니다. Windows와 Linux에서 같은 ZIP을 사용합니다. Python 3.12는 Linux에서 ZIP을 푸는 예시에만 사용하며, 스킬 실행에는 필요하지 않습니다.

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.pi\packages" | Out-Null
Expand-Archive .\ponytail-pi-offline-4.10.3.zip -DestinationPath "$HOME\.pi\packages" -Force
pi install "$HOME\.pi\packages\ponytail"
```

## Linux

```sh
mkdir -p "$HOME/.pi/packages"
python3.12 -m zipfile -e ponytail-pi-offline-4.10.3.zip "$HOME/.pi/packages"
pi install "$HOME/.pi/packages/ponytail"
```

Pi의 로컬 경로 설치는 이 폴더를 **제자리에서** 읽습니다. 설치 후 `ponytail` 폴더를 옮기지 마세요. Pi가 실행 중이면 `/reload`를 실행하거나 다시 시작합니다. `pi list`에서 설치 항목을 확인할 수 있습니다.

기본 모드는 `full`이며 코딩 작업마다 자동으로 적용됩니다. `/ponytail lite`, `/ponytail full`, `/ponytail ultra`, `/ponytail off`로 바꿀 수 있습니다. `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`도 사용할 수 있습니다. 자동 적용을 끄고 필요할 때만 켜려면 Pi를 시작하기 전에 `PONYTAIL_DEFAULT_MODE=off`를 설정합니다.

이 패키지는 원본 Pi 확장과 6개 스킬, 확장에 필요한 설정 파일, 원본 README·벤치마크, MIT 라이선스를 포함합니다. 외부 API나 네트워크 호출을 추가하지 않습니다. [출처](PROVENANCE.md)를 참고하세요.
