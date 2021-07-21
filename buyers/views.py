from django.shortcuts import render
from buyers.models import Buyer
from buyers.serializers import BuyerSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class BuyerViewSet(ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
