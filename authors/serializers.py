from rest_framework.serializers import HyperlinkedModelSerializer
from authors.models import Author


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
