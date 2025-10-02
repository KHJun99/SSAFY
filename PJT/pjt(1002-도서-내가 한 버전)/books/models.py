# books/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    # 제목/저자는 CharField에 적절한 max_length 부여 (폼/DB 제약)
    title = models.CharField(max_length=100)      # 기존: max_length 누락 → 추가
    author = models.CharField(max_length=100)     # 기존: TextField → 검색/정렬 고려해 CharField로
    description = models.TextField()

    # 평점은 0~5로 한정(명세 추정) → 유효성 검증기 부착
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    # 공통 메타/표현 (정렬/가독성)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성시각
    updated_at = models.DateTimeField(auto_now=True)      # 수정시각

    def __str__(self):
        return f"{self.title} · {self.author}"

    class Meta:
        ordering = ['-created_at']  # 최신순 출력
