# 번들 출처

- kordoc 4.18.8: https://github.com/chrisryugj/kordoc, 커밋 `d15ee77d717e0670947d80b082aa5d7fa54eb249`, npm 패키지 무결성 `sha512-/rrl2vTfAwS2kb3Vn41TYjPsE4c7isgGvFMTthcmSD2gBnDQW5zGctYD3JxiLJ6ZkggGIoJZV5rVvrTBuFlhnw==`
- Node.js 22.16.0 Linux x64 공식 배포 파일 SHA-256: `f4cb75bb036f0d0eddf6b79d9596df1aaab9ddccd6a20bf489be5abe9467e84e`
- Node.js 22.16.0 Windows x64 공식 배포 파일 SHA-256: `21c2d9735c80b8f86dab19305aa6a9f6f59bbc808f68de3eef09d5832e3bfbbd`
- `pdfjs-dist` 4.10.38과 kordoc 런타임 의존성은 npm에서 설치한 파일을 함께 담았습니다. 선택적 네이티브 의존성과 개발 의존성은 제외했습니다.

번들 내부의 `node_modules/`와 `runtime/`은 위 배포물에서 가져왔으며, `SKILL.md`와 `scripts/kordoc.py`는 이 저장소에서 Pi용으로 작성했습니다.
