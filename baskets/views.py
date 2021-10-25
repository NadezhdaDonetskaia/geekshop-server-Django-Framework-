from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Baskets


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Baskets.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Baskets.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, product_id):
    basket = Baskets.objects.filter(id=product_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
