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

    def save(self):
        # user = self.validated_data['user']
        # product = self.validated_data['product']

        product_id = self.data['product']

        participants = Funding.objects.filter(product_id=product_id).count()
        fund_per_once = Product.objects.filter(id=product_id).get().fund_per_once
        total_fund = participants * fund_per_once

        Product.objects.filter(id=product_id).update(total_fund=total_fund)