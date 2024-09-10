from rest_framework import viewsets
from .models import Category, PrintshopService, PrintshopOrder
from .serializers import CategorySerializer, PrintshopServiceSerializer, PrintshopOrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PrintshopServiceViewSet(viewsets.ModelViewSet):
    queryset = PrintshopService.objects.all()
    serializer_class = PrintshopServiceSerializer


class PrintshopOrderViewSet(viewsets.ModelViewSet):
    queryset = PrintshopOrder.objects.all()
    serializer_class = PrintshopOrderSerializer
