from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import filters

from .models import User

from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)
