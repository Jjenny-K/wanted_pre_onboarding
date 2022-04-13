from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer