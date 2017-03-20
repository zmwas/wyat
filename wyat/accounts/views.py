from django.contrib.auth import login


from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response



from .models import User
from .serializers import UserSerializer,TokenSerializer
from .permissions import IsAnonCreate

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAnonCreate,
    ]
