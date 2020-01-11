from django.shortcuts import render
from products.models import Product

# Create your views here.
def search_products(request):
    queryset = Product.objects.filter(name__icontains=request.Get['q'])
    return render(request, "products.html", {"products": queryset})