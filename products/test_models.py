from django.test import TestCase
from products.models import Product
from django.shortcuts import reverse



# Create your tests here.
class TestModels(TestCase):

    def test_str_method_returns_string(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

    def test_fields(self):
        product = Product()
        product.name = 'Product name'
        product.description = 'Product description'
        product.save()

        record = Product.objects.get(pk=1)
        self.assertEqual(record, product)

    
        
class TestProductModels(TestCase):   

    @classmethod
    def setUp(cls):
        Product.objects.create(name='This is a test')

    def test_to_create_new_products(self):
        product = Product.objects.get(id=1)
        expected_product_name = product.name
        self.assertEqual(expected_product_name, 'This is a test')