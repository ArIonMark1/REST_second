from  rest_framework.serializers import HyperlinkedModelSerializer
from users.models import BaseUser


class BaseUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff',  'is_superuser', 'last_login'
