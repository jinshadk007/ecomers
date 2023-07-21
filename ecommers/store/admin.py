from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_name', 'product_image', 'description', 'stock', 'is_available', 'original_price',
                    'offer_price', 'modified_date']
    list_editable = ['product_image', 'description', 'stock', 'is_available', 'original_price', 'offer_price']
    prepopulated_fields = {'slug': ('product_name',)}



admin.site.register(Product, ProductAdmin)

# Register your models here.
