from django.db import models
from django.forms import ModelForm

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.email
    


    