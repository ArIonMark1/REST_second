from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from books.models import Book
from books.serializers import BooksSerializer


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
