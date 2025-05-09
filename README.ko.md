
<div align="center">
<a href="https://www.nonead.com">
<img src="https://www.nonead.com/assets/img/vi/NONEAD_ai.png" width="300" alt="nonead logo">
</a>
</div>

<p align="center">
  <a href="./README.en.md">English</a> |
  <a href="./README.md">简体中文</a> |
  <a href="./README.jp.md">日本語</a> |
  <a href="./README.ko.md">한국어</a> |
  <a href="./README.de.md">Deutsch</a> |
  <a href="./README.fr.md">Français</a> |
  <a href="./README.ru.md">Русский язык</a> |
  <a href="./README.th.md">ภาษาไทย</a> |
  <a href="./README.es.md">Español</a> |
  <a href="./README.ar.md">العربية</a> |
  <a href="./README.da.md">dansk</a>  
</p>

<p align="center">
    <a href='https://gitee.com/nonead/nUR_MCP_SERVER'><img src='https://img.shields.io/github/v/release/nonead/nUR_MCP_Server?color=green&label=Latest%20Release' alt="Latest Release"></a>
    <a href="https://github.com/nonead/nUR_MCP_SERVER/releases/latest"><img src="https://img.shields.io/github/v/release/nonead/nUR_MCP_Server?color=blue&label=Latest%20Release" alt="Latest Release"></a>
    <a href='https://www.python.org/downloads/'><img src='https://img.shields.io/pypi/pyversions/RPALite'></img></a>
    <a href="https://gitee.com/nonead/nUR_MCP_SERVER/wikis/pages">
        <img src="https://img.shields.io/badge/User%20Guide-1e8b93?logo=readthedocs&logoColor=f5f5f5" alt="User Guide"></a>
    <a href="https://www.apache.org/licenses/LICENSE-2.0"><img height="21" src="https://img.shields.io/badge/License-Apache--2.0-ffffff?labelColor=d4eaf7&color=2e6cc4" alt="license"></a>
     <a href='https://gitee.com/nonead/nUR_MCP_SERVER/stargazers'><img src='https://gitee.com/nonead/nUR_MCP_SERVER/badge/star.svg?theme=dark' alt='star'></img></a>

</p>

## 1. MCP란?
MCP(모델 컨텍스트 프로토콜)는 Anthropic사가 개발한 통신 프로토콜(2024년 11월 오픈소스화)로, AI 대형 언어 모델(DeepSeek-V3-0324, DeepSeek-R1, Qwen3 등)이 외부 데이터/도구/서비스에 효율적으로 접근하여 더 정확하고 지능적인 답변을 제공하기 위해 사용됩니다.

MCP 주요 기능

컨텍스트 정보 제공:
앱이 파일/DB 내용 등 추가 정보 전달
예: 보고서를 AI가 읽고 내용 기반 답변

외부 도구 연동:
파일 조작/DB 조회/API 호출/하드웨어 제어 등 직접 제어
예: 문서 자동 정리, DB 데이터 기반 보고서 생성

지능형 워크플로우 구축:
다중 MCP 서비스 조합으로 데이터 분석 자동화/고객 지원 등 구현

데이터 보안:
로컬 환경 운영으로 민감 데이터 보호

## 2. MCP 작동 원리
클라이언트-서버 구조

MCP 클라이언트: AI 앱(요청 발신)
MCP 서버: 데이터/도구 인터페이스 제공
통신: JSON-RPC 2.0 표준(실시간 알림 지원)

## 3. MCP 서버 주요 기능
데이터 접근:
파일/DB/메모리 데이터 제공

도구 실행:
SQL 조회/파일 저장 기능 제공

실시간 업데이트:
데이터 변경 시 AI 알림

세션 관리:
연결 상태 관리

## 2. nUR MCP 서버 핵심 기능  

### 2.1 UR 로봇의 모든 하드웨어 데이터 수집  
**네트워크 스캔 기능**  
fY6gJ6KcwVqfiiUFO-ogx1: 지정된 IP 범위에서 UR 로봇 스캔  

**연결 관리 기능**  
fCf-PPsfx_yD_iZLURtGTV: 지정된 IP의 UR 로봇에 연결  
fEd1Yp4RD3kiUSxqQlK1Va: UR 로봇 연결 해제  

**기본 정보 수집**  
fmMqIRbJZ4qRGJtRd59OJ-: 로봇 시리얼 번호 가져오기  
f1ITpGFuwNDVfGfkNJzG2z: 소프트웨어 버전 가져오기  
f8RnXWPeoSCCCvW3FuF_vS: 가동 시간 가져오기  
fl_BhgXwRaQ8nzexSGjwa7: 안전 모드 가져오기  

**레지스터 데이터 수집**  
fRRbXKNWy6vXbSrRPmFLJa: Int 레지스터 값(0-23) 가져오기  
fRjcTzBeNogyaJtYvJ7_E2: Double 레지스터 값(0-23) 가져오기  
fJ_s1E0ywr6t9rkMOBWiq6: Double 레지스터 값(0-31) 가져오기  

**상태 모니터링**  
fVYZ0ocbfuml1VpA5JSNRo: 실시간 TCP 좌표 가져오기  
fts21SISQrnyp_mb3jJy91: 실시간 관절 각도 가져오기  
fmjZNwC7zxju_tLjiM8w4A: 작동 상태 가져오기  
fy5NIEBXN7Kqecb1RkPhZN: 프로그램 실행 상태 가져오기  

**전기 파라미터 모니터링**  
fGU3ubp1fmrw-zPE2pyNDI: 현재 전압 가져오기  
fl--FA0LvH9LBjXjVB0gGD: 현재 전류 가져오기  
fb3HhLwWUa8s49OXpU5Iq8: 각 관절 전압 가져오기  
frGKnkZFPFesyEXdGAxpD9: 각 관절 전류 가져오기  
fzVxBGVvO7T3n3JbmAmvqB: 각 관절 온도 가져오기  

### 2.2 UR 로봇 단일 명령 실행  
**운동 제어 기능**  
ffoF99tQZ6vcEqHQplHTjv: 관절 위치 명령 전송(movej)  
fiF4Pmxs7LQTrG7hY4sQV8: TCP 직선 이동 명령 전송(movel)  
fOyQY2wR6xzOZP3NxjpLjK: X축 직선 이동  
fCV_0M8pdPIVJs3nMGo6XS: Y축 직선 이동  
fWkTyW-C5rxUPe3U0WGSsm: Z축 직선 이동  

### 2.3 대형 언어 모델로 UR 로봇 스크립트 프로그램 작성 및 실행  

### 2.4 UR 로봇 내장 프로그램 실행  
**프로그램 제어**  
fE0WxXcDh3ENo8Q3fYul5K: UR 프로그램 로드  
fDqpZeOA1_KF8ixwndRP8-: UR 프로그램 로드 및 실행  
fH1AYKDXPCcGU1q3Ndrnwt: 현재 프로그램 정지  
fVwECQj8_p85mT6KaggA-N: 현재 프로그램 일시 정지  
f4cp0iAFlVXMWqz51ylP4Z: 프로그램 스크립트 전송  

### 2.5 다중 UR 로봇 연동  


## 3. 면책사항

nUR MCP Server 사용 전, 운영 담당자가 UR 로봇 안전 교육을 이수하고 비상정지(E-stop) 등 안전 조작에 숙련되었는지 반드시 확인하십시오.

로봇 및 MCP Server 운영 상태를 정기적으로 점검하여 시스템 안정성과 안전성을 확보할 것을 권장합니다.

nUR MCP Server 사용 시 다음 안전 규정을 엄격히 준수해야 합니다:

로봇 가시 범위 내 운영

운영자는 언제나 유니버설 로봇이 시야 내에 위치하도록 하여 실시간 모니터링이 가능해야 합니다.

로봇 작동 중 작업 구역 이탈을 금지하며, 사고 발생 시 신속히 대응할 수 있도록 합니다.

작업 환경 안전 확보

로봇 가동 전 주변 장애물을 점검 및 제거하고, 위험 구역에 인원/장비/기타 물체가 진입하지 않도록 하십시오.

필요 시 물리적 방벽 또는 안전 광센서를 설치하여 무단 접근을 방지합니다.

안전 규정 위반 시 책임 면제

상기 안전 요건(감시 소홀, 작업 구역 미정리 등)을 준수하지 않아 인적 상해, 장비 손상 또는 생산 사고가 발생할 경우, 당사는 법적 책임 및 배상 의무를 지지 않습니다.

모든 운영 위험과 결과는 사용자 측에서 부담합니다.


## 4. 버전 릴리스

### 4.1 최근 업데이트

* 2025.05.15 : nUR_MCP_SERVER 첫 출시

### 4.2 향후 계획

* nUR MCP Server 전용 MCP Client 지원, 실행기 보안 기능 강화
* UR 로봇 로그 기록 추가
* UR 로봇 프로그램 백업 및 업로드

## 5. 빠른 시작

### 5.1 제품 기반 (일반 사용자용)

#### 5.1.1 엔진 & 종속성

* **권장 시스템 버전:**

  ```text
  macOS 사용자: macOS Monterey 12.6 이상
  Linux 사용자: CentOS 7 / Ubuntu 20.04 이상
  Windows 사용자: Windows 10 LTSC 2021 이상
  ```

* **소프트웨어 요구사항:**

  MCP 서버 환경

  ```text
  Python 3.11 이상     
  pip 25.1 이상
  UV Package Manager 0.6.14 이상  
  bun 1.2.8 이상
  ```

  MCP 클라이언트

  ```text
   Claude Desktop 3.7.0 이상
   Cherry Studio 1.2.10 이상
   Cline 3.14.1 이상

   ClaudeMind, Cursor, NextChat, ChatMCP, Copilot-MCP, Continue, Dolphin-MCP, Goose는 테스트되지 않았습니다.
  ```

   LLM 대형 언어 모델

  ```text
  DeepSeek-V3-0324 이상
  DeepSeek-R1-671b  이상 
  Qwen3-235b-a22b 이상
  
  일반적으로 MCP를 지원하는 대형 언어 모델은 사용 가능하며, 목록 이외의 모델은 테스트되지 않았습니다.
  Ollama로 배포된 모델은 현재 Tool 호출이 불가능하며, 해결 중입니다...
  ```

#### 5.1.2 설치

**MCP 서버 설치:**
1. Python 3.11 이상 설치
2. pip 25.1 이상 설치
3. UV Package Manager 0.6.14 이상 설치
4. bun 1.2.8 이상 설치
5. MCP Server 설치:
```
     git clone https://gitee.com/nonead/nUR_MCP_SERVER.git
     cd nUR_MCP_SERVER
     pip install -r requirements.txt
```

**MCP 클라이언트 설정:**

**Claude Desktop과 함께 사용하려면 서버 설정을 추가하세요:**
MacOS: ~/Library/Application Support/Claude/claude_desktop_config.json  

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
          "command": "python",
          "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
        }
      }
    }

Windows: %APPDATA%/Claude/claude_desktop_config.json  

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
          "command": "cmd",
          "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
        }
      }
    }

**Cherry Studio와 함께 사용하려면 서버 설정을 추가하세요：**  

**macOS & Linux용:**  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "name": "nUR_MCP_Server",
      "type": "stdio",
      "description": "NONEAD Universal-Robots MCP Server",
      "isActive": true,
      "provider": "NONEAD Corporation",
      "providerUrl": "https://www.nonead.com",
      "logoUrl": "https://www.nonead.com/assets/img/vi/5.png",
      "tags": [
        "NONEAD",
        "nUR_MCP_Server",
        "Universal-Robots"
      ],
      "command": "python",
      "args": [
        "/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"
      ]
    }
  }
}
```

**Windows용:**  
```
{
  "mcpServers": {
    "nUR_MCP_SERVER": {
      "name": "nUR_MCP_Server",
      "type": "stdio",
      "description": "NONEAD Universal-Robots MCP Server",
      "isActive": true,
      "provider": "NONEAD Corporation",
      "providerUrl": "https://www.nonead.com",
      "logoUrl": "https://www.nonead.com/assets/img/vi/5.png",
      "tags": [
        "NONEAD",
        "nUR_MCP_Server",
        "Universal-Robots"
      ],
      "command": "cmd",
      "args": [
        "/c",
        "python",
        "D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"
      ]
    }
  }
}
```

**Cline과 함께 사용하려면 서버 구성을 추가하세요:**
MacOS & Linux:

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
            "command": "python",
            "args": ["/home/nonead/MCP_Server/nUR_MCP_SERVER/main.py"]
         }
      }
    }

Windows:

    {
      "mcpServers": {
        "nUR_MCP_SERVER": {
            "command": "cmd",
            "args": ["/c","python","D:\\MyProgram\\MCP_SERVER\\nUR_MCP_SERVER\\main.py"]
         }
      }
    }


### 5.2 툴킷 기반 (개발자용)

#### 5.2.1 엔진 & 의존성 

* **권장 시스템 버전:**

  ```text
  macOS 사용자: macOS Monterey 12.6 이상
  Linux 사용자: CentOS 7 / Ubuntu 20.04 이상
  Windows 사용자: Windows 10 LTSC 2021 이상
  ```

* **소프트웨어 요구사항:**

  MCP 서버 환경

  ```text
  Python 3.11 이상     
  pip 25.1 이상
  UV Package Manager 0.6.14 이상  
  bun 1.2.8 이상
  ```
  LLM 대형 언어 모델

  ```text
  DeepSeek-V3-0324 이상
  DeepSeek-R1-671b 이상 
  Qwen3-235b-a22b 이상
  
  일반적으로 MCP를 지원하는 대형 언어 모델은 사용 가능합니다. 목록 외 모델은 테스트되지 않았습니다
  Ollama로 배포된 모델은 현재 Tool 호출이 불가능합니다. 해결 중입니다...
  ```

#### 5.2.2 설치

**macOS/Linux/Windows 개발자용**

```text
Python 3.11 이상
pip 25.1 이상
UV 패키지 관리자 0.6.14 이상
bun 1.2.8 이상
```

#### 5.2.3 사용 방법

다음은 대형 언어 모델이 수행할 수 있는 작업 예시입니다:

* 유니버설 로봇 IP 연결: 192.168.1.199
* 유니버설 로봇 TCP 엔드 이펙터 현재 포즈 좌표 획득
* nUR_MCP_SERVER 도구의 모든 명령어 목록 표시
* 유니버설 로봇의 모든 하드웨어 데이터 획득
* 유니버설 로봇 스크립트 프로그램 실행
* 유니버설 로봇 내장 프로그램 XXXX.urp 실행
* IP 172.22.109.141 로봇을 A, IP 172.22.98.41 로봇을 B로 지정 후 연결. A(왼쪽)와 B(오른쪽)의 현재 TCP 포즈 및 각 키 포지션 기록, 두 로봇 포즈 상관관계 분석
* 단계적 실행: IP 192.168.1.199 로봇에서 현재 TCP 포즈 기록 후 +Z 방향 20mm, -Y 방향 50mm, +X 방향 30mm 이동을 5회 반복
* 유니버설 로봇 스크립트 작성 및 실행: 현재 포즈를 중심으로 베이스 평면에 반경 50mm 원 그리기
* IP 172.22.109.141을 A, 172.22.98.41을 B로 설정 후 연결. 이후 명령은 A만 제어하며 B에 미러 동작 동기화

## 6. 기술 아키텍처

MCP는 클라이언트-서버 아키텍처를 채택, 표준화 프로토콜로 모델과 외부 리소스 간 통신 구현.  
![alt](./images/MCP.svg "mcp")  
클라이언트-서버 모델
MCP 아키텍처 주요 구성요소:

MCP 호스트: 연결을 시작하는 LLM 애플리케이션(Claude Desktop 또는 IDE 등)
MCP 클라이언트: 호스트 앱 내 서버와 1:1 연결 유지 프로토콜 클라이언트
MCP 서버: 표준화 Model Context Protocol로 특정 기능 노출 경량 프로그램
로컬 데이터 소스: MCP 서버가 안전하게 접근 가능한 컴퓨터 파일/DB/서비스
원격 서비스: MCP 서버가 연결 가능한 API 기반 외부 시스템
주요 구성요소 책임:

MCP 호스트:
UI 제공
LLM 공급자 연결 관리
외부 리소스 접근을 위한 MCP 클라이언트 통합
MCP 클라이언트:
MCP 서버와 연결 수립/유지
요청 전송/응답 수신
MCP 프로토콜 표준 준수 데이터 교환 처리
MCP 서버:
클라이언트 요청 처리
특정 기능 실행/리소스 접근 제공
MCP 프로토콜 표준 준수 응답 형식화
통신 프로토콜
MCP는 JSON-RPC 2.0을 기본 통신 프로토콜로 사용:  
![alt](./images/p.svg "mcp_json-RPC2.0")   
요청: 클라이언트→서버/서버→클라이언트 작업 시작 메시지
응답: 요청에 대한 회신(결과/오류 정보 포함)
알림: 응답 불필요 단방향 메시지(주로 이벤트 알림용)
MCP 지원 전송 메커니즘:

표준 입출력(Stdio): 로컬 서버용, 프로세스 간 통신 구현
Server-Sent Events(SSE): HTTP 기반 전송 메커니즘, 원격 서버용

MCP 장점
MCP는 기존 통합 방법 대비 통일성·보안성·확장성에서 뛰어난 장점 보유.

통일성
표준화된 AI 시스템과 외부 데이터 소스 상호작용으로 기존 단편화 문제 해결:

플러그인식 접속: 통일 프로토콜로 다양한 데이터 소스 플러그인 접속 가능
크로스 플랫폼 호환: 서로 다른 AI 모델/플랫폼 지원
개발 단순화: 개발자는 비즈니스 로직에 집중 가능
보안성
내장 보안 메커니즘으로 데이터 전송/처리 과정 보호:

민감 정보 보호: API 키/사용자 데이터 등 민감 정보 보호
접근 제어: MCP 서버에서 세밀한 접근 제어 구현
로컬 처리: 민감 정보를 제3자에 업로드 없이 로컬 처리
확장성
모듈러 설계로 높은 확장성 구현:

멀티 서비스 연결: 여러 서비스가 호환 클라이언트에 연결 가능
생태계 확대: 성숙화에 따라 이용 가능한 사전 제작 컴포넌트 증가
커스터마이즈 능력: 개발자는 필요 시 커스텀 MCP 서버 생성 가능 

## 7. 연락처

**GitHub**: <https://github.com/nonead/nUR_MCP_SERVER>  
**gitee**: <https://gitee.com/nonead/nUR_MCP_SERVER>  
**공식 웹사이트**: <https://www.nonead.com>  

<img src="./images/QR.gif" alt="연락처: Nonead Tech WeChat" width="200">  

## 8. nUR MCP 서버와 다른 MCP 서버의 차이점

nUR MCP 서버를 사용하는 사용자는 매우 높은 안전 의식을 가지고 있어야 하며, 유니버설 로봇 사용 교육을 받아야 합니다. 대형 언어 모델이 조작하는 것은 실제 로봇이며, 부적절한 조작은 인신 피해와 재산 손실을 초래할 수 있으므로 반드시 주의하십시오.

## 9. 인용

본 소프트웨어를 사용하는 경우 아래와 같이 인용해 주세요:

* [nURMCP: NONEAD Uninversal-Robots Model Context Protocol Server](https://www.nonead.com)
* 탁덕은 지능 제조의 진수를 보여주며, 혁신으로 세계를 바꿉니다 <br>
  Nonead demonstrates the true meaning of intelligent manufacturing, pioneering innovations that reshape our world.

## 10. 라이선스

[Apache License 2.0](LICENSE)

## 11. 개발 핵심 팀

수저우 탁덕 로봇 기술 유한회사 MCP 서버 개발 팀

**Tony Ke** <tonyke@nonead.com>  
**Micro Zhu** <microzhu@nonead.com>  
**Anthony Zhuang** <anthonyzhuang@nonead.com>  
**Quentin Wang** <quentinwang@nonead.com>
