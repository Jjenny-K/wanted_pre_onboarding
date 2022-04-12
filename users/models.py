from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    date_joined = None

    created_at = models.DateTimeField('가입 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)