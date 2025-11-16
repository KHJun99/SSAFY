# 07-pjt: Django REST API 프로젝트

## 프로젝트 개요
영화 정보를 제공하는 RESTful API 서버 구현

## 기술 스택
- Python 3.11
- Django 5.2
- Django REST Framework

## 프로젝트 구조
```
mypjt/
├── mypjt/              # 프로젝트 설정 디렉토리
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── movies/             # movies 앱
│   ├── models.py       # Actor, Movie, Review 모델
│   ├── serializers.py  # Serializer 클래스들
│   ├── views.py        # API view 함수들
│   └── urls.py         # URL 패턴
├── actors.json         # 배우 초기 데이터
├── movies.json         # 영화 초기 데이터
├── reviews.json        # 리뷰 초기 데이터
├── requirements.txt
└── README.md
```

## 설치 및 실행 방법

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 초기 데이터 로드
```bash
python manage.py loaddata actors.json
python manage.py loaddata movies.json
python manage.py loaddata reviews.json
```

### 5. 서버 실행
```bash
python manage.py runserver
```

## API 엔드포인트

### 배우(Actor)
- `GET /api/v1/actors/` - 전체 배우 목록 조회
- `GET /api/v1/actors/<actor_id>/` - 단일 배우 상세 조회

### 영화(Movie)
- `GET /api/v1/movies/` - 전체 영화 목록 조회
- `GET /api/v1/movies/<movie_id>/` - 단일 영화 상세 조회

### 리뷰(Review)
- `GET /api/v1/reviews/` - 전체 리뷰 목록 조회
- `GET /api/v1/reviews/<review_id>/` - 단일 리뷰 조회
- `PUT /api/v1/reviews/<review_id>/` - 리뷰 수정
- `DELETE /api/v1/reviews/<review_id>/` - 리뷰 삭제
- `POST /api/v1/movies/<movie_id>/reviews/` - 영화에 리뷰 작성

## 모델 구조

### Actor
- id: 배우 ID (자동 생성)
- name: 배우 이름

### Movie
- id: 영화 ID (자동 생성)
- title: 영화 제목
- overview: 줄거리
- release_date: 개봉일
- poster_path: 포스터 경로
- actors: 출연 배우 (M:N 관계)

### Review
- id: 리뷰 ID (자동 생성)
- title: 리뷰 제목
- content: 리뷰 내용
- movie: 대상 영화 (N:1 관계)

## 구현된 필수 기능
- ✅ F01: 프로젝트 및 앱 구성
- ✅ F02: Actor 모델 구현
- ✅ F03: Movie 모델 구현
- ✅ F04: Review 모델 구현
- ✅ F05: Serializer 클래스 구현
- ✅ F06: actor_list view 구현
- ✅ F07: actor_detail view 구현
- ✅ F08: movie_list view 구현
- ✅ F09: movie_detail view 구현
- ✅ F10: review_list view 구현
- ✅ F11: review_detail view 구현
- ✅ F12: create_review view 구현

## 테스트 방법
Postman이나 브라우저를 통해 다음 URL에 접근하여 테스트할 수 있습니다:
- http://127.0.0.1:8000/api/v1/actors/
- http://127.0.0.1:8000/api/v1/movies/
- http://127.0.0.1:8000/api/v1/reviews/

feat : login 개발
feat : model 개발

docs : readme 업데이트

bug : bug 수정

