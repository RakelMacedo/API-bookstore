from rest_framework.viewsets import ModelViewSet

from product.models.product import Category
from product.serializers.product_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()