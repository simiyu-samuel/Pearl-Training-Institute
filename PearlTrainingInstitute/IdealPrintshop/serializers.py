from rest_framework import serializers
from .models import Category, PrintshopService, PrintshopOrder


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PrintshopServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = PrintshopService
        fields = '__all__'


class PrintshopOrderSerializer(serializers.ModelSerializer):
    service = PrintshopServiceSerializer()

    class Meta:
        model = PrintshopOrder
        fields = '__all__'
