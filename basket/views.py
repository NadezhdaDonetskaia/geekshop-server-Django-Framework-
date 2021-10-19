from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from products.models import Product
from basket.models import Basket


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_product(request, product_id):
    product = Basket.objects.filter(id=product_id)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




