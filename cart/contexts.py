from django.shortcuts import get_object_or_404
from products.models import Product


def cart_products(request):
    """
    Displays the numbers of items to show it in all pages
    """
    cart = request.session.get('cart',{})
    cart_items = []
    total = 0
    number_of_items = 0
    for id, quantity in cart.items():
        item = get_object_or_404(Product, pk=id)
        total += quantity * item.price
        number_of_items += quantity
        if cart_items in cart_products:
            total = quantity + quantity
        else:
            cart_items.append({'id':id, 'quantity':number_of_items, 'item':item})
    
    return {'cart_items': cart_items, 'total': total, 'number_of_items': number_of_items}