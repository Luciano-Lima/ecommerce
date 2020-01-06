from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    """Testing that all the fields in the Post models return a value """
    def create_product(self, name='A product', description=' product description', price='product price', image="product image"):
        return Create_produt.objects.create(name=name, description=description, price=price, image=image)
        
