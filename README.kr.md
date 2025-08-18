# Ask The Clock

[[English](README.md)]

`ask-the-clock` 은 당신이 결정을 내리는 데 도움을 주는 프로그램입니다.

## 기능
- 이 프로그램은 하드웨어 기반의 난수를 생성합니다. 생성된 숫자가 5 이상이면 *Yes*를, 5 미만이면 *No*를 반환합니다.

## 사용법
```shell
> ask-the-clock 오늘 치킨을 먹어야 할까
Yes
```

하나 이상의 질문을 인자로 전달하여 결정을 내리거나, 인자 없이 실행하여 즉각적인 답변을 받을 수 있습니다.

## 설치
### macOS
Homebrew를 사용하여 `ask-the-clock` 을 설치할 수 있습니다.

```shell
brew tap chebread/ask-the-clock

brew install ask-the-clock
```

### 그 외 운영체제
1. `ask-the-clock` 의 [GitHub Releases 페이지](https://github.com/chebread/ask-the-clock/releases)에 방문합니다.
2. 운영 체제와 아키텍처에 맞는 파일을 다운로드합니다.
3. 다운로드한 파일의 압축을 해제합니다.
4. `ask-the-clock` 실행 파일을 실행합니다.
5. 좀 더 쉽게 접근하려면, `ask-the-clock` 실행 파일을 시스템의 PATH 환경 변수에 추가하는 것을 고려해 보세요.

## 업데이트
### macOS
Homebrew로 ask-the-clock을 설치했다면, 간단한 명령어로 최신 버전을 유지할 수 있습니다.

```shell
brew upgrade ask-the-clock
```

### 그 외 운영체제
다른 운영체제의 경우, `ask-the-clock` 의 [GitHub Releases 페이지](https://github.com/chebread/ask-the-clock/releases)에서 새로운 버전을 직접 다운로드해야 합니다.

최신 릴리스를 다운로드하여 기존의 실행 파일을 새 파일로 교체하세요.

## 라이선스
MIT LICENSE &copy; 2025 Cha Haneum