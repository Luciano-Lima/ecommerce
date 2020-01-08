from django.conf.urls import url
from .views import view_cart, add_to_cart, update_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^update/(?P<id>\d+)', update_cart, name='update_cart'),
]