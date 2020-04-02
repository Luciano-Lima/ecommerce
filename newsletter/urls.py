from django.conf.urls import url
from .views import newsletter


urlpatterns = [
    url(r'^sign_in/', newsletter, name='newsletter_signin')
]
    
    