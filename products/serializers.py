from rest_framework import serializers
from .models import Product, Funding

class ProductCreateListSerializer(serializers.ModelSerializer):
    # 게시자
    publisher = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Product
        fields = ['title', 'publisher', 'description', 'target_fund', 'end_date', 'fund_per_once',
                  'total_fund', 'achievement_rate', 'd_day']
        read_only_fields = ['total_fund']

class ProductDetailSerializer(serializers.ModelSerializer):
    # 게시자
    publisher = serializers.ReadOnlyField(source='user.username')
    # 참가자 수
    participants = serializers.SerializerMethodField('get_participants')

    class Meta:
        model = Product
        fields = ['title', 'publisher', 'description', 'target_fund', 'end_date', 'fund_per_once',
                  'total_fund', 'achievement_rate', 'd_day', 'participants']
        read_only_fields = ['target_fund', 'total_fund']

    def get_participants(self, obj):
        return Funding.objects.filter(product_id=obj.id).count()

class FundingSerializer(serializers.ModelSerializer):
    # 상품 정보
    product_name = serializers.ReadOnlyField(source='product.title')
    # 펀딩 참여자 정보
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Funding
        fields = '__all__'

    # 유저가 상품 펀딩시, 총 펀딩 금액(total_fund) 수정 로직 추가
    # 펀딩 저장 로직 수정 필요
    # 총 펀딩 금액 수정시 예외 처리 필요
    def save(self):
        # user = self.validated_data['user']
        # product = self.validated_data['product']

        product_id = self.data['product']

        total_fund = Product.objects.filter(id=product_id).get().total_fund
        fund_per_once = Product.objects.filter(id=product_id).get().fund_per_once
        total_fund += fund_per_once

        Product.objects.filter(id=product_id).update(total_fund=total_fund)