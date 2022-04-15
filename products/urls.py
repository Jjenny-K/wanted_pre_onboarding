from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "products"

router = DefaultRouter()
router.register('product', views.ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]