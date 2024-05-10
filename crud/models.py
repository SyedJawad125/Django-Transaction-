from django.db import models

# Create your models here.

class Orders(models.Model):

    total_price = models.PositiveBigIntegerField()
    delivered_at = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()


class Orderdetials(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    ordersdel = models.CharField(max_length=100, null=True, blank=True)
    Timestamps = models.DateTimeField(auto_now_add=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='products_order_detials', null=True, blank=True)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE,related_name='orders1', null=True, blank=True)
 