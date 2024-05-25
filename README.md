# KakaoTalk Text Mining

## Description

카카오톡 대화 내용을 텍스트 마이닝하여 워드 클라우드를 생성한다.

## Prerequisite

1. 가상환경 생성

- macOS

```shell
python3 -m venv .venv
```

- Windows

```shell
python -m venv .venv
```

2. 가상환경 활성화

- macOS

```shell
source ./.venv/bin/activate
```

- Windows

```shell
.\.venv\Scripts\activate.bat
```

3. 패키지 설치

```shell
pip3 install -r requirements.txt
```

4. pc 카카오톡에서 대화기록을 csv 형식으로 저장

- csv 파일 예시
  ```
  Date,User,Message
  2023-10-21 12:56:59,"user1","안녕"
  ```

## Usage

- 프로그램 실행 (`file_path`: `.csv` 파일 경로)

```shell
python3 main.py <file_path>
```
