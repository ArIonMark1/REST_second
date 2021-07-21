from books.models import Book
from rest_framework.serializers import HyperlinkedModelSerializer


class BooksSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
