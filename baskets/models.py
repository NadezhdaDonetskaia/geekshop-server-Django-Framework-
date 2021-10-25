from django.db import models
from users.models import User
from products.models import Product


class Baskets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина {self.user.username} | Товары {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def get_baskets(self):
        return Baskets.objects.filter(user=self.user)

    def total_sum(self):
        return sum(float(basket.sum()) for basket in self.get_baskets())

    def total_quantity(self):
        return sum(basket.quantity for basket in self.get_baskets())
