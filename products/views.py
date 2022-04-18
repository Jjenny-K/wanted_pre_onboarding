from rest_framework import viewsets, filters
from .serializers import ProductCreateListSerializer, ProductDetailSerializer, FundingSerializer
from .models import Product, Funding

# Create your views here.

class ProductCreateListAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreateListSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['title', 'description']
    ordering = ['id']
    ordering_fields = ['created_at', 'total_fund']

class ProductDetailAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'product_id'

class FundingAPI(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    lookup_url_kwarg = 'product_id'