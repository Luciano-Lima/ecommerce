from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def index(request):
    """Return index.html file"""
    return render(request, 'index.html')


def login(request):
    """Log the user in or Return the login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are loged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Username or password is incorrect")
        else:
            login_form = UserLoginForm()
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def logout(request):
    """Log the user out """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))


def register(request):
    """Render the user registration form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST) 
        if registration_form.is_valid():
            #Saving the user to the database
            registration_form.save()
            #Log the authenticated user in
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully been registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Please check all details and try again...")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})


def user_profile(request):
    """User profile page"""
    #Retrieves the user from the database based on email
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})