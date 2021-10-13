from django.shortcuts import render
from products import models


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
        'products': models.Product.objects.all()
    }
    return render(request, 'products/products.html', context)

