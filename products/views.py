from django.db.models import Count
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            participants = Count('funding')
        )
