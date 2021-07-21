from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authors.models import Author
from authors.serializers import AuthorSerializer


# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
