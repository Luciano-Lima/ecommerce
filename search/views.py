from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_products(request):
    products_items = Product.objects.all().order_by('name')
    query = request.GET.get('q')
    if query:
        products_items = Product.objects.filter(name__icontains=query).order_by('name')
    paginator = Paginator(products_items, 2)
    page = request.GET.get('page')
    try: 
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1) #returns the first page if page not integer
    except EmptyPage:
        product = paginator.page(paginator.num_pages) #returns last page if page out of range
    
    return render(request, "home.html", {"products": product})
