from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from authors.models import Author
from users.serializers import BaseUserSerializer


class AuthorSerializer(HyperlinkedModelSerializer):
    # user = BaseUserSerializer(many=True)

    class Meta:
        model = Author
        fields = 'user',
