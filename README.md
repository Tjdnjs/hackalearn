# 💥hackalearn - maracom💥

### [Go To MoCL Page](https://mento-maracom.herokuapp.com)

- [도입](#Introduce)
  - [팀 소개](#MARACOM)
  - [협업 방식](#user-content-협업-방식)
  - [프로젝트 소개](#user-content-mento-of-college-life-mocl)

- [설계](#설계)
  - [Frontend](#Frontend)
  - [Backend](#Backend)
- [개발 일정](#user-content-개발-일정)

## Introduce

## MARACOM

---

**박서원 (PM - Fullstack)**

- python flask
- mysql
- html
- css

login/logout<br>게시글 CR<br>댓글 CR<br>DataBase<br>배포

---

**이채원 (Dev - Frontend)**

- html
- css

index.html<br>write.html<br>detail.html

---

**조윤주(Dev - Frontend)**

- html
- css

answer.html<br>login.html<br>question.html

---

## 협업 방식

### GitHub 코드공유

Pull Request 를 통한 코드 공유를 통해 서로의 개발 현황을 확인

![image](https://user-images.githubusercontent.com/91242806/185753324-7be297d9-477a-4d01-96d7-981540e11c91.png)
![image](https://user-images.githubusercontent.com/91242806/185753327-84d9d079-48e3-435e-8fc5-0a32b7422e6b.png)

### Google Meet 회의

전체 회의 7회 : 7/27, 8/1, 8/2, 8/7, 8/9, 8/12, 8/15

각 주에 개발할 내용을 구체적으로 기획하고, 중간점검과 최종점검 진행. 중간점검 / 최종 점검을 할 때에는 화면을 공유하며 채친과 음성으로 읙녀을 주고받고, 피드백에 따른 실시간 수정을 진행함

필요시 2인 회의 추가 진행

![image](https://user-images.githubusercontent.com/91242806/185753206-16eb4af0-235c-4a3c-9027-973d3fe7412b.png)

### KakaoTalk 개발 일정 정리 및 피드백

각 주에 정해진 개발 내용을 체크박스 형태로 정리하여 완료될 시 하나씩 체크하며 프론트 / 백의 개발 업무 현황 확인 

Fetch 과정에서 충돌이 발생할 시 또는 작은 피드백을 공유할 시 카톡으로 대화를 나눔

![image](https://user-images.githubusercontent.com/91242806/185753390-b864135f-c56c-4a49-b4f0-c8db538bb0cf.png)

## Mento of College Life (MoCL)

### [Go To MoCL Page](https://mento-maracom.herokuapp.com)

- [주제 선정 배경](#user-content-주제-선정-배경)
- [기능](#기능)

### 주제 선정 배경

대학 생활 중 좋은 프로그램이 많지만, 그 프로그램을 참여하기 위해 어떠한 준비과정을 거쳐야하는 지에 대한 정보는 얻기 힘들다. 하여, 해당 경험이 있는 멘토를 통해 원하는 정보를 얻을 수 있는 사이트 제작을 기획하게 되었다.

### 기능

1. 로그인 / 로그아웃
2. 게시글 작성 / 열람 
3. 댓글 작성 / 열람
4. 게시글 카테고리 분류 자동화
5. 게시글 / 댓글 작성 권한을 로그인 된 사용자에게만 부여

## 설계

### Frontend

MoCL의 메인 페이지로, 서비스에 대한 소개와 더불어 핵심 기능인 질문 / 답변 페이지로 연결됩니다

메인 페이지의 디자인에 맞추어 서브 페이지들을 설계하였으며, [html](https://github.com/Tjdnjs/hackalearn/tree/main/templates) , [css](https://github.com/Tjdnjs/hackalearn/tree/main/static/css) 파일은 각각 해당 링크에서 확인하실 수 있습니다.

![image](https://user-images.githubusercontent.com/91242806/184681109-9bac6d54-97f6-42d2-8657-959ab8a6a029.png)

### Backend

Python의 flask 라이브러리와 mysql 데이터베이스를 활용하여 개발을 진행하였습니다

[app.py](https://github.com/Tjdnjs/hackalearn/blob/main/app.py) <- 해당 링크에서 코드를 확인하실 수 있습니다.

## 개발 일정

## 1️⃣ 7/28 ~ 8/2

### 강의

|Stack|Lecture|
|:---|:---|
|Front|Code it - HTML/CSS 시작하기<br>Code it - HTML/CSS 핵심 개념<br>Code it - 반응형 웹 퍼블리싱|
|Back|Inflearn - 가장 빠른 풀스택 (Python flask)<br>섹션 0. 강의 준비 ~ 섹션 4. 파이썬 flask 기본과 웹기술<br><br>Inflearn - SQL/DB(MySQL)<br>섹션 0. 수업 준비 및 환경 설치 ~ 섹션 2. 데이터베이스 만들기|

### 개발 진행 상황

|Stack|Status|
|:---|:---|
|Front|index.html, login.html, question.html, header 틀 제작|
|Back|페이지 routing / login, logout 기능 구현 <br>데이터베이스 구조 기획|

## 2️⃣ 8/3 ~ 8/9

### 강의

|Stack|Lecture|
|:---|:---|
|Front|Code it - 인터랙티브 자바스크립트<br>Code it - 모던 자바스크립트|
|Back|Inflearn - 가장 빠른 풀스택 (Python flask)<br>섹션 5. flask로 백/프론트 구현하기 ~ 섹션 7. 다양한 flask 백엔드 기능<br><br>Inflearn - SQL/DB(MySQL)<br>섹션 3. 데이터 다루기 (CRUD) ~ 섹션 4. 파이썬으로 다루는 MySQL (pymysql)|

### 개발 진행 상황

|Stack|Status|
|:---|:---|
|Front|index.html 수정<br>write.html, answer.html 메뉴바 제작|
|Back|게시글 CR 구현<br>로그인 된 사용자만 글 작성 가능하도록 수정<br>앱 및 데이터베이스 배포|

## 3️⃣ 8/10 ~ 8/16

### 개발 진행 상황

|Stack|Status|
|:---|:---|
|Front|index.html 디자인 수정<br>answer.html 게시판 추가, sidemenu 디자인 수정<br>detail.html css 제작<br>write.html 게시판 정보 추가 및 css 변경<br>|
|Back|댓글 CR 구현<br>카테고리 자동화|
