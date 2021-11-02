from django.contrib import admin
from products.models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # отображение полей в продуктах
    list_display = ('name', 'price', 'quantity', 'category')
    # расположение полей в продукте
    fields = ('name', 'images', 'description', ('price', 'quantity'), 'category')
    # сортировка по имени
    ordering = ('name',)
    # поиск по
    search_fields = ('name',)
