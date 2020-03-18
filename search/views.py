from django.shortcuts import render
from products.models import Product

# Create your views here.
def search_products(request):
    queryset = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "home.html", {"products": queryset})
    
