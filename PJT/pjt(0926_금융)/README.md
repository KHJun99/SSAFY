# 관통프로젝트(0926) — **stockpjt / crawlings**

> **개요:** Django(5.x) + Selenium을 이용해 토스증권 커뮤니티 댓글을 수집·저장하고, 웹에서 조회/삭제 기능을 제공하는 미니 프로젝트.
> **핵심 흐름:** `/crawlings/index/`(검색) → `/crawlings/list/`(목록/삭제)
> **비고:** 본 구현은 **AI 보조(코드 생성/디버깅 지원)**를 활용해 제작되었다.

---

## 0. 데모 화면

* **검색 페이지:** 회사명 입력 후 “검색” → Selenium 크롤링 수행
* **목록 페이지:** 상단에 `회사명 (종목코드)` 표기, 하단에 수집 댓글 리스트 및 항목별 삭제 버튼
* **UI 특징:** 헤더/히어로/카드형 리스트 구성, 본문 16px + line-height 1.8, 지브라 효과로 가독성 강화

---

## 1. 기술 스택

* **Language:** Python 3.11+
* **Web:** Django 5.x (개발 서버)
* **Crawler:** Selenium 4.6+ (selenium-manager 또는 webdriver-manager)
* **DB:** SQLite (Django 기본)
* **Front:** Django 템플릿(HTML/CSS), 심플·반응형 톤

> 개발 서버 경고(“WARNING: This is a development server…”)는 정상 동작이며, 배포 시 WSGI/ASGI 서버 사용 권장.

---

## 2. 폴더 구조

```
stockpjt/
├─ manage.py
├─ stockpjt/                # settings.py / urls.py / wsgi.py
└─ crawlings/
   ├─ models.py             # Comment 모델
   ├─ views.py              # index / fetch / list / delete
   ├─ urls.py               # 앱 URLConf
   ├─ services.py           # Selenium 크롤러(검색→코드 추출→커뮤니티→댓글 수집)
   └─ templates/crawlings/
      ├─ base.html          # 공통 레이아웃
      ├─ index.html         # 검색 페이지
      └─ list.html          # 결과(목록/삭제)
```

---

## 3. 빠른 시작(로컬)

```bash
# 가상환경
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 의존성
pip install -r requirements.txt

# DB
python manage.py makemigrations
python manage.py migrate

# 실행
python manage.py runserver
# → http://127.0.0.1:8000/crawlings/index/
```

**Selenium 드라이버 초기화 참고**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)
```

> Selenium 4에서는 `service=` 인자를 사용하는 형태가 권장된다.

---

## 4. 요구사항 구현 요약

| 기능     | URL                       | 내용                                       |
| ------ | ------------------------- | ---------------------------------------- |
| F01 입력 | `/crawlings/index/`       | 회사명(종목명) 입력 폼 → `POST /crawlings/fetch/` |
| F02 수집 | `/crawlings/fetch/`       | 토스증권 검색→종목코드 추출→커뮤니티 이동→댓글 수집→DB 저장      |
| F03 목록 | `/crawlings/list/`        | 저장 댓글 목록 출력, 상단 `회사명 (종목코드)` 표시          |
| F04 삭제 | `/crawlings/delete/<pk>/` | 댓글 삭제(POST), 삭제 후 동일 컨텍스트 유지             |

**데이터 모델**

```python
class Comment(models.Model):
    company_name = models.CharField(max_length=100)
    stock_code   = models.CharField(max_length=20)
    content      = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
```

---

## 5. 구현 단계 & 참고

* **프로젝트/앱 생성:** `startproject stockpjt`, `startapp crawlings`
* **라우팅:** 프로젝트 `urls.py` ↔ 앱 `urls.py` 분리, 루트(`/`)는 `/crawlings/index/`로 리다이렉트 구성 가능
* **뷰 구성:** `index(검색, GET) / fetch(수집, POST) / list(목록, GET) / delete(삭제, POST)`
* **템플릿:** `base.html` 상속으로 공통 레이아웃 유지, `index.html`/`list.html`은 콘텐츠 블록만 구현
* **ORM:** `bulk_create()`로 다건 저장, `order_by("-id")`로 최근순 정렬, `get_object_or_404()`로 안전한 단건 접근
* **CSRF:** 모든 POST 폼에 `{% csrf_token %}` 적용

---

## 6. 주요 이슈 & 해결

1. **TypeError: `WebDriver.__init__() got multiple values for argument 'options'`**

   * 원인: Chrome 드라이버 경로를 **위치 인자**로 전달 시 Selenium 4에서 `options` 충돌
   * 해결: `webdriver.Chrome(service=Service(...), options=opts)` 패턴으로 수정

2. **동적 로딩 지연**

   * 해결: `WebDriverWait(...).until(EC.presence_of_element_located(...))`로 명시적 대기 적용

3. **선택자 변동성**

   * 대응: 핵심 구간(검색창/게시글/댓글)에 대체 선택자 준비(XPath/여러 후보)

4. **CSS 파싱 오류(빨간 줄)**

   * 원인: 복붙 시 제로폭/nbsp 등 숨은 문자 혼입
   * 해결: VSCode 정규식 치환 `[\u00A0\u200B\u200C\u200D\u2060\uFE0F\uFEFF]` → 빈 문자열 치환, 또는 해당 라인 재타이핑

5. **루트 404**

   * 해결: 프로젝트 `urls.py`에서 루트→`crawlings:index` 리다이렉트

---

## 7. 검증 시나리오

1. `/crawlings/index/` 접속 → “삼성전자” 입력 → **검색**
2. 크롤링 완료 후 `/crawlings/list/?company=삼성전자&code=005930` 이동
3. 댓글 리스트 확인, 항목별 **삭제** 기능 점검
4. 공백 입력/오타 등 예외 시 에러 메시지 표시 확인

---

## 8. 유지보수 & 확장 제안

* **선택자 회복력:** 다중 셀렉터·폴백 경로·DOM 헬스체크
* **데이터 품질:** 중복 제거, 이모지/공백 정규화, 불용어 처리
* **분석 확장:** 간단 감성분석/요약 결과를 배지로 표시(긍·부·중립)
* **필터/검색:** 기간/키워드/종목코드 필터, 페이지네이션
* **스케줄링:** APScheduler/Celery Beat에 의한 정기 수집 및 알림
* **내보내기:** CSV/JSON 다운로드

---

## 9. 준수 사항(크롤링 윤리/법적)

* 대상 서비스 **이용약관/robots** 준수
* 요청 빈도 제한 및 지연(Throttle)로 서비스 부하 방지
* 수집·저장 데이터는 목적상 **최소한**으로 한정

---

## 10. 트러블슈팅 체크리스트

* 브라우저/드라이버 버전 확인: `pip show selenium`, Chrome 버전 일치 여부
* `Broken pipe` 로그: 사용자 중단 시 발생 가능(핵심 이슈 아님)
* 크롤링 실패: 네트워크/VPN/사이트 구조 변경 여부 점검
* CSS 깨짐: 숨은 문자 제거 후 강력 새로고침(CTRL+F5)

---

## 11. AI 협업을 통해 알게 된 점

> 본 프로젝트는 **AI 코드 생성·디버깅 보조**를 활용해 구현되었으며, 다음은 AI와의 협업 과정에서 정리된 학습 포인트입니다.

---

### 11.1 Django 설계/패턴
- **라우팅/진입 동선**: AI가 `/` → `/crawlings/index/` 리다이렉트를 제안하여 초기 진입 UX를 단순화.
- **역할 분리**: `index(검색)/fetch(수집)/list(목록)/delete(삭제)`로 **HTTP 메서드 단위** 책임 분리를 권장(`@require_http_methods`, `@require_POST`).
- **템플릿 상속**: 공통 레이아웃(`base.html`) 도입으로 페이지 간 디자인 **일관성·재사용성**을 확보.
- **안전한 ORM 사용**: 다량 저장 시 `bulk_create()` 사용, 단건 처리엔 `get_object_or_404()` 채택을 권고.
- **컨텍스트 유지 전략**: 조회 페이지에서 `company`/`code`를 **쿼리스트링**으로 유지해 삭제 후에도 같은 맥락을 이어가도록 설계.

---

### 11.2 Selenium 실전 포인트
- **드라이버 초기화 규약(Selenium 4)**:  
  `webdriver.Chrome(service=Service(...), options=opts)` 형태를 사용해야 하며, 드라이버 경로를 **위치 인자**로 넘기면 `options` 중복 전달 오류가 발생한다는 점을 AI가 지적.
- **명시적 대기 사용 이유**: 동적 로딩 대비로 `WebDriverWait(...).until(EC.presence_of_element_located(...))`를 기본값처럼 쓰도록 제안.
- **스크롤 수집 루프**: `scrollHeight` 변화를 감지하여 **추가 로드 종료** 조건을 두는 패턴을 안내.
- **선택자 변동성 대응**: 클래스명이 자주 바뀌는 사이트 특성상 **대체 선택자(XPath/여러 후보)**를 준비하라는 가이드를 제공.

---

### 11.3 UI/접근성(가독성 중심)
- **카드형 리스트 + 지브라 효과**: 긴 댓글을 빠르게 스캔하기 위해 배경/테두리/줄간격(16px, line-height 1.8) 조합을 제안.
- **본문/메타 분리**: 댓글 본문과 `회사/종목코드/작성시각` 메타라인을 구분하여 정보 구조를 명확히 하라는 권장.
- **작은 시각 앵커**: 항목 좌측의 **dot 인디케이터**로 리스트 시작점을 고정해 읽기 흐름을 개선.

---

### 11.4 디버깅 & 트러블슈팅
- **`multiple values for 'options'` 오류**: Selenium 4 시그니처 변경을 AI가 정확히 짚어 해결 방향(Service 객체 사용)을 제시.
- **루트 404**: 프레임워크 기본 라우팅 동작을 설명하고, 루트 리다이렉트로 UX를 보완하도록 유도.
- **복붙으로 인한 CSS 파싱 오류**: 제로폭/nbsp 등 **숨은 문자**를 정규식(`[\u00A0\u200B\u200C\u200D\u2060\uFE0F\uFEFF]`)으로 제거하는 실전 요령을 제공.
- **로그 판별**: `Broken pipe`는 본질 이슈가 아님을 구분(사용자 중단 시 발생)하도록 안내.

---

### 11.5 제품/운영 관점
- **MVP 우선 접근**: 입력→수집→저장→목록/삭제의 **핵심 플로우**를 먼저 완성하고, 분석/필터/내보내기 등은 단계적으로 확장하라는 로드맵을 제시.
- **에러 표면화**: 서버 500으로 삼키지 말고, 화면에 **명확한 실패 사유**를 전달하라는 UX 원칙을 강조.
- **크롤링 윤리**: 약관·robots, 요청 간격(Throttle), 수집 최소화 등 기본 준수사항을 상기.

---

### 11.6 AI 활용 자체에 대한 메타 학습
- **프롬프트 전략**: 에러 로그 **원문**, **환경/버전**, **재현 절차**를 함께 제공하면 해결 속도와 정확도가 크게 향상.
- **생성 코드 검증**: AI가 제시한 코드라도 **로컬 재현 테스트**와 **단계적 실행 로그**로 확인하는 습관이 중요.
- **대안 탐색**: 같은 문제를 **여러 방식**으로 질문(예: “원인 가설→검증 절차→패치 코드”)하면 더 견고한 솔루션을 도출.

