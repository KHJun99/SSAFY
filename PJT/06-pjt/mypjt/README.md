# 06-pjt: 영화 커뮤니티 서비스

## 프로젝트 개요
Django를 사용하여 영화 데이터를 생성, 조회, 수정, 삭제(CRUD)할 수 있는 웹 애플리케이션입니다.
영화에 대한 댓글 기능도 포함되어 있습니다.

## 개발 환경
- Python 3.11
- Django 5.2
- Bootstrap 5.3
- SQLite3

## 프로젝트 구조
```
mypjt/
├── config/              # 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── movies/              # movies 앱
│   ├── migrations/      # 마이그레이션 파일
│   ├── templates/       # 템플릿 파일
│   │   └── movies/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── create.html
│   │       ├── detail.html
│   │       └── update.html
│   ├── models.py        # Movie, Comment 모델
│   ├── forms.py         # MovieForm, CommentForm
│   ├── views.py         # 뷰 함수
│   ├── urls.py          # URL 설정
│   └── admin.py         # 관리자 설정
└── manage.py
```

## 주요 기능

### 필수 기능 (F01-F11)

#### 1. 프로젝트 및 앱 구성 (F01)
- 프로젝트명: mypjt
- 앱 이름: movies
- Navbar를 통한 페이지 이동

#### 2. Model 클래스 (F02, F03)
**Movie 모델**
- title: 영화 제목
- description: 줄거리
- director: 감독
- genre: 장르 (액션, 코미디, 공포 중 선택)
- score: 평점 (0~5점, 0.5점 단위)

**Comment 모델**
- content: 댓글 내용
- movie: Movie와 1:N 관계 (ForeignKey)

#### 3. Form 클래스 (F04)
- MovieForm: Movie 모델을 위한 ModelForm
- CommentForm: Comment 모델을 위한 ModelForm
- Bootstrap 스타일 적용

#### 4. View 함수

**index (F05)**
- URL: `/movies/`
- 전체 영화 목록 조회
- 각 영화의 detail 페이지 링크 제공

**create (F06)**
- URL: `/movies/create/`
- GET: 영화 등록 폼 제공
- POST: 영화 데이터 저장 후 detail 페이지로 redirect
- 데이터 유효성 검사

**detail (F07)**
- URL: `/movies/<int:pk>/`
- 단일 영화 상세 정보 조회
- UPDATE, DELETE 버튼
- 댓글 목록 및 작성 UI

**update (F08)**
- URL: `/movies/<int:pk>/update/`
- GET: 기존 데이터가 입력된 수정 폼 제공
- POST: 수정된 데이터 저장 후 detail 페이지로 redirect

**delete (F09)**
- URL: `/movies/<int:pk>/delete/`
- POST 요청으로만 삭제 가능
- 삭제 후 index 페이지로 redirect

**comments_create (F10)**
- URL: `/movies/<int:pk>/comments/`
- POST 요청으로 댓글 저장
- 저장 후 해당 영화 detail 페이지로 redirect

**comments_delete (F11)**
- URL: `/movies/<int:movie_pk>/comments/<int:comment_pk>/delete/`
- POST 요청으로 댓글 삭제
- 삭제 후 해당 영화 detail 페이지로 redirect

### 비기능적 요구사항

#### URL 구성 (NF02)
- app_name과 name을 사용한 URL 역참조
- 유지보수 용이성 확보

#### HTTP Method 허용 (NF03)
- `@require_safe`: GET, HEAD만 허용 (index, detail)
- `@require_POST`: POST만 허용 (delete, comments_create, comments_delete)
- `@require_http_methods`: GET과 POST만 허용 (create, update)

## 설치 및 실행

### 1. 패키지 설치
```bash
pip install django==5.2
```

### 2. 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 관리자 계정 생성 (선택)
```bash
python manage.py createsuperuser
```

### 4. 서버 실행
```bash
python manage.py runserver
```

### 5. 접속
- 메인 페이지: http://127.0.0.1:8000/movies/
- 관리자 페이지: http://127.0.0.1:8000/admin/

## 구현 상세

### URL 패턴
```python
movies/                                    # 영화 목록
movies/create/                             # 영화 등록
movies/<int:pk>/                           # 영화 상세
movies/<int:pk>/update/                    # 영화 수정
movies/<int:pk>/delete/                    # 영화 삭제
movies/<int:pk>/comments/                  # 댓글 작성
movies/<int:movie_pk>/comments/<int:comment_pk>/delete/  # 댓글 삭제
```

### 데이터베이스 관계
```
Movie (1) ─────< (N) Comment
```

## 학습 내용

### Django Model과 ORM
- Model 클래스 정의 및 필드 타입 이해
- ForeignKey를 통한 1:N 관계 구현
- related_name을 통한 역참조

### Django Form
- ModelForm을 통한 데이터 유효성 검사
- Form 위젯 커스터마이징
- 에러 메시지 처리

### Django View
- 함수 기반 뷰(Function Based View) 구현
- HTTP Method 데코레이터 활용
- redirect와 render의 차이

### Django Template
- 템플릿 상속 (extends, block)
- URL 역참조 (url 태그)
- 템플릿 필터 활용 (truncatewords 등)
- 템플릿 태그 (for, if, empty 등)

### Bootstrap
- Bootstrap 5.3 활용한 UI 구성
- 반응형 디자인
- Form 스타일링

## 어려웠던 점

1. **1:N 관계 구현**
   - ForeignKey의 on_delete 옵션 이해
   - related_name을 통한 역참조 방법

2. **HTTP Method 제한**
   - 각 기능에 적절한 HTTP Method 선택
   - 데코레이터를 통한 제한 구현

3. **URL 설계**
   - RESTful한 URL 패턴 구성
   - app_name과 name을 통한 URL 역참조

## 새로 배운 것

1. Django의 MTV(Model-Template-View) 패턴
2. ORM을 통한 데이터베이스 조작
3. ModelForm을 통한 폼 처리
4. 데코레이터를 통한 HTTP Method 제한
5. Bootstrap을 활용한 빠른 UI 구성

## 느낀 점

Django의 강력한 기능들을 활용하여 빠르게 웹 애플리케이션을 구축할 수 있었습니다.
특히 ModelForm과 템플릿 상속 기능이 개발 생산성을 크게 향상시킨다는 것을 체감했습니다.
앞으로는 사용자 인증 기능과 이미지 업로드 기능을 추가하여 더욱 완성도 높은 서비스를 만들어보고 싶습니다.
