from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # "user" is the user profile
    email = models.EmailField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return "{0}".format(self.user.username)
    
    

    