from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "users"

# url 자동 생성
router = DefaultRouter()
router.register('user', views.UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]