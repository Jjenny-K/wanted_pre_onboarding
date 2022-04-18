from django.utils.timezone import now
from django.db import models
from users.models import User

# Create your models here.

# 상품 정보
class Product(models.Model):

    title = models.CharField('제목', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField('상품 설명')
    target_fund = models.IntegerField('목표 금액', default=0)
    end_date = models.DateTimeField('펀딩 종료일')
    fund_per_once = models.IntegerField('1회 펀딩 금액', default=0)
    total_fund = models.IntegerField('총 펀딩 금액', default=0)
    created_at = models.DateTimeField('등록 날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정 날짜', auto_now=True)

    # 달성률
    @property
    def achievement_rate(self):
        return self.total_fund // self.target_fund * 100

    # D-day
    @property
    def d_day(self):
        return (self.end_date.date() - now().date()).days

# 펀딩 정보
class Funding(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField('펀딩 날짜', auto_now_add=True)