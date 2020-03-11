from django.conf.urls import url, include
from .views import index, categories
# from . import views
from products.models import Product



urlpatterns = [
    url(r'^$', index, name='home_page'),
    url(r'^(?P<category_slug>[-\w]+)/$', categories, name='products_by_category'),
    
]