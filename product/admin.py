from django.contrib import admin

# Register your models here.
from .models.category import Category
from .models.product import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "active")


admin.site.register(Product, ProductAdmin)
