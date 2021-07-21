from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import BaseUser
from users.serializers import BaseUserSerializer


# Create your views here.

class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
