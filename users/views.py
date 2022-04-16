from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer