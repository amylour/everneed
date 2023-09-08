from django.contrib import admin
from .models import Product, Category 


class CategoryAdmin(admin.ModelAdmin):
    """ Class to access Category model in Django Admin panel """
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    """ Class to access the Products model in Django Admin panel """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'sale_price',
        'discount',
        'has_sizes',
        'is_shoe',
        'carbon_fp',
        'carbon_saved',
        'rating',
        'image_url',
        'image',
        'feature_product',
        'is_sale',
    )

    ordering  = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
