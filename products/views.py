from rest_framework import viewsets, filters
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    filter_fields = ['created_at', 'total_fund']
    search_fields = ['title', 'description']
    ordering = ['id']
    ordering_fields = ['created_at', 'total_fund']

