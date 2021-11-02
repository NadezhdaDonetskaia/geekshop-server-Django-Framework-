from django.contrib import admin

from baskets.models import Baskets


class BasketAdmin(admin.TabularInline):
    model = Baskets
    fields = ('product', 'quantity')
    # убирает лишние поля в отображении продуктов в корзине у пользователя
    extra = 0
