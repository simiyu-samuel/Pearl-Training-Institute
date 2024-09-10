from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PrintshopServiceViewSet, PrintshopOrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'services', PrintshopServiceViewSet)
router.register(r'orders', PrintshopOrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
