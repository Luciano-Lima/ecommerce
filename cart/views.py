from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import messages

# Create your views here.
def view_cart(request):
    """Render the cart page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add items to cart"""
    quantity = int(request.POST.get('quantity') or 0)
    if quantity == 0:
        messages.warning(request,'Please enter a quantity!')
        
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    request.session['cart'] = cart
    return redirect(reverse('index'))
        
    


def update_cart(request, id):
    """Add or Remove itens from the cart"""
    quantity = int(request.POST.get('quantity')or 0)#prevents literal for int() error
    if quantity == 0:  
        messages.warning(request,'Enter a new Quantity or Proceed to Checkout!')
        # return redirect(reverse('checkout'))
    else:
        cart = request.session.get('cart',{})
        products = Product.objects.all()
        if quantity >= 0:
            cart[id] = quantity
            messages.success(request,'Your cart was updated sucessfully!')
        else:
            cart.pop(id)
        request.session['cart'] = cart
    return redirect(reverse('view_cart'))


  
def delete_cart(request, id):
    quantity = int(request.POST.get('quantity')or 0)
    cart = request.session.get('cart',{})
    products = Product.objects.all()
    if quantity >= 0:
        cart.pop(id)
        request.session['cart'] = cart
        messages.success(request,'Item removed from your Cart!')
    return redirect(reverse('view_cart'))
    