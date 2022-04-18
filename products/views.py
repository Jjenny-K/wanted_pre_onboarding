from rest_framework import viewsets, filters
from .serializers import ProductCreateListSerializer, ProductDetailSerializer, FundingSerializer
from .models import Product, Funding

# Create your views here.

# 상품 등록, 목록
class ProductCreateListAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreateListSerializer

    # 상품 검색, 정렬 기능
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    # 검색
    search_fields = ['title', 'description']
    # 정렬
    ordering = ['id']
    ordering_fields = ['created_at', 'total_fund']

# 상품 상세, 수정, 삭제
class ProductDetailAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'product_id'

# 상품 펀딩
class FundingAPI(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    lookup_url_kwarg = 'product_id'