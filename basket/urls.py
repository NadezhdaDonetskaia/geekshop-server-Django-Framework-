from django.urls import path
from basket.views import basket_add, remove_product

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:product_id>/', remove_product, name='remove_product'),
]
