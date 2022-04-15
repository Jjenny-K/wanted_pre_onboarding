from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # 게시자
    publisher = serializers.ReadOnlyField(source='username')

    # 참가자 수
    participants = serializers.IntegerField()

    class Meta:
        model = Product
        # fields = ['title', 'publisher', 'description', 'target_fund', 'fund_per_once', 'end_date']
        fields = '__all__'
        read_only_fields = ('publisher', 'participants')
