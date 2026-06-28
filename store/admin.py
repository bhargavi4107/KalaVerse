from django.contrib import admin
from .models import Product, Order

admin.site.register(Product)
admin.site.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "art_form",
        "price",
        "stock",
        "featured",
    )

    list_filter = (
        "category",
        "featured",
        "experience_level",
    )

    search_fields = (
        "name",
        "art_form",
        "brand",
    )

    ordering = ("name",)
