from django.db import models
from products.models import Product
from django import forms

# Create your models here.
class Order(models.Model):
    # Gathering the costumer information on checkout
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=50, blank=False)
    post_code = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    date = models.DateField()
    
    

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.name, self.date)

class ProductOrdered(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)