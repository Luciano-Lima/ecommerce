from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # "user" is the user profile
    email = models.EmailField(max_length=200, blank=False)
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=50, blank=False)
    post_code = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return "{0}".format(self.user.username)
    
    

    