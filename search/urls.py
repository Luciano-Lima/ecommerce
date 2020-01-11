from django.conf.urls import url
from .views import search_products

urlpatterns = [
    url(r'^$', search_products, name='search')
]
