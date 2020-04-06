from django.test import TestCase
from checkout.forms import OrderForm


# Create your tests here.
class TestOrderForm(TestCase):

    def test_field_name_is_required(self):
        form = OrderForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_is_not_required(self):
        form = OrderForm({'name': 'This field is required'})
        self.assertFalse(form.is_valid())
