from django.test import TestCase
from newsletter.views import newsletter
from django.shortcuts import reverse


# Create your tests here.
class TestNewlettersViews(TestCase):

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse(newsletter))
        self.assertEqual(response.status_code, 200)

    def test_get_newsletter_template(self):
        response = self.client.get(reverse(newsletter))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
