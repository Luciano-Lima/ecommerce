from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Login the user in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """New user registration form"""
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter password:", widget=forms.PasswordInput)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        #Check if the user already exists
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email already exists, please choose another one:')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        #check for a empty password field
        if not password1 or not password2:
            raise ValidationError('Please confirm your password:')
        #check if the password match
        if password1 != password2:
            raise ValidationError('Password must match:')
        return password2