from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 필수 요구사항은 AbstractUser 상속만 요구
    # (도전과제 F18 확장 필드는 여기서 추후 추가 가능)
    pass
