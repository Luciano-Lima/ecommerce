from django.conf.urls import url, include
from .views import home
# from . import views
from products.models import Product



urlpatterns = [
    url(r'^$',home, name='home'),
    url(r'^(?P<category_slug>[-\w]+)/$', home, name='products_by_category'),
    
]