from django import forms
from .models import Newsletter

# Newsletter form
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
