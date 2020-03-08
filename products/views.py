from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Returns all products in the database
def home(request, category_slug=None):
    category = None
    products = None
    if category_slug!=None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all().filter()
    return render(request, "products.html", {"category": category, "products": products})


