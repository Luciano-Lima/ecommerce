from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Product, Category


#returns all the products in the database
def index(request):
    products = Product.objects.all() 
    return render(request, "home.html", {"products": products})
    


# Returns all products and display in the home page by category
def categories(request, category_slug=None):
    category = None
    products = None
    if category_slug!=None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all().filter()
    return render(request, "products.html", {"category": category, "products": products})


