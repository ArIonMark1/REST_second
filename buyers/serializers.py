from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from buyers.models import Buyer


class BuyerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
