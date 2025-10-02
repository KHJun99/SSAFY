from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])  # 0~5
    author = models.CharField(max_length=120)

    # 도전 F17 확장: author_info, author_works 필드는 이후 추가 가능
    # author_info = models.TextField(blank=True)
    # author_works = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
