from django.contrib import admin
from .models import Product, Category, Origin, Size


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'origin',
        'sku',
        'name',
        'has_sizes',
        'price',
        'intensity',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class OriginAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Origin)
