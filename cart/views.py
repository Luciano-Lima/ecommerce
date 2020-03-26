from django.shortcuts import render, redirect, reverse
from products.models import Product

# Create your views here.
def view_cart(request):
    """Render the cart page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add items to cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    request.session['cart'] = cart
    return redirect(reverse('index'))


def update_cart(request, id):
    """Add or Remove itens from the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart',{})
    products = Product.objects.all()
    if quantity >= 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
       