from rest_framework.relations import StringRelatedField

from authors.serializers import AuthorSerializer
from books.models import Book
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class BooksSerializer(HyperlinkedModelSerializer):
    # author = AuthorSerializer(many=True)
    # author = StringRelatedField()

    class Meta:
        model = Book
        fields = 'title', 'description', 'release_year', 'author',
