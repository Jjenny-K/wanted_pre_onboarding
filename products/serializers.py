from django.db.models import Count
from django.utils.timezone import now
from rest_framework import serializers
from .models import Product, Funding

class ProductSerializer(serializers.ModelSerializer):
    # 게시자
    publisher = serializers.ReadOnlyField(source='user.username')
    # 참가자 수
    participants = serializers.SerializerMethodField('get_participants')
    # 총 펀딩 금액
    total_fund = serializers.SerializerMethodField('get_total_fund')
    # 펀딩 달성률
    achievement_rate = serializers.SerializerMethodField('get_achivement_rate')
    # 펀딩 종료일까지 d-day
    d_day = serializers.SerializerMethodField('get_d_day')

    class Meta:
        model = Product
        # fields = ['title', 'publisher', 'description', 'target_fund', 'fund_per_once', 'end_date']
        fields = '__all__'
        # read_only_fields = ('publisher', 'participants', 'total_fund', 'achievement_rate', 'd_day')

    def get_participants(self, obj):
        return Funding.objects.filter(product_id=obj.id).count()

    def get_total_fund(self, obj):
        participants = Funding.objects.filter(product_id=obj.id).count()
        return participants * obj.fund_per_once

    def get_achivement_rate(self, obj):
        total_fund = Funding.objects.filter(product_id=obj.id).count() \
                     * obj.fund_per_once
        return total_fund // obj.target_fund * 100

    def get_d_day(self, obj):
        return (obj.end_date.date() - now().date()).days