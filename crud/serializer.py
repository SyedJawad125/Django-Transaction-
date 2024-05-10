from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderdetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetials
        fields = '__all__'