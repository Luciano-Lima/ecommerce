from django.test import TestCase
from cart.views import view_cart
from products.models import Product
from django.shortcuts import reverse


# Create your tests here.
class TestViews(TestCase):
    def test_get_view_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html') 

    def test_add_to_cart(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html') 

    
    def test_update_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_delete_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')


    def test_empty_cart_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    


    
