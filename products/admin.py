"""
Product App Amin Classes
"""
from django.contrib import admin
from .models import Product, Category, Origin


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    list_display = (
        'category',
        'origin',
        'sku',
        'name',
        'price',
        'intensity',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


class OriginAdmin(admin.ModelAdmin):
    """
    Origin Admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Origin, OriginAdmin)
