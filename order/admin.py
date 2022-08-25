from django.contrib import admin

# Register your models here.
from .models.order import Order

admin.site.register(Order)