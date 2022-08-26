from django.urls import path, include
from rest_framework import routers

from product.viewsets.product_viewset import ProductViewSet
from product.viewsets.category_viewset import CategoryViewSet

router = routers.SimpleRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
