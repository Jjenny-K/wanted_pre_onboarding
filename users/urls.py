from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "users"

router = DefaultRouter()
router.register('user', views.UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]