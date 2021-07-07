from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, related_name='products')
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.title

    def get_total_price(self):
        return self.product.price * self.amount
