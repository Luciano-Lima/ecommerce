from django.conf.urls import url, include
from .views import index, logout, login, register, profile
from users import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
