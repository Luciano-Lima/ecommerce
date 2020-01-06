from django.conf.urls import url, include
from .views import returns_all_products

urlpatterns = [
    url(r'^$',returns_all_products, name='products'),

]