from django.config.urls import url
from .views import checkout


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]