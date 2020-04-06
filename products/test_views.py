from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    
    def test_can_get_product_view_template(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        