from django.shortcuts import render, redirect, reverse
from .models import Newsletter
from .forms import NewsletterForm
from django.contrib import messages

# Create your views here.

def newsletter(request):
    signup = NewsletterForm(request.POST or None)
    if signup.is_valid():
        instance = signup.save(commit=False) #create a instance variable to check for already subscribed emails
        if Newsletter.objects.filter(email=instance.email).exists():
            messages.warning(request,"You are already subscribed!")
            return redirect('index')
        else:
            instance.save()
            messages.success(request, "Thanks for subscribing!")
            return redirect('newsletter_signin') 
    return render(request, 'sign_up.html', {'signup': signup})
    