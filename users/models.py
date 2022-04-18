from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 유저 정보 커스텀
class User(AbstractUser):

    # 본래 User 모델에서 사용하지 않을 field 지정
    date_joined = None

    created_at = models.DateTimeField('가입 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)