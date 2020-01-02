from django.conf.urls import url, include
from .views import index, logout, login, register, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
