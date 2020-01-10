from django.shortcuts import get_object_or_404
from products.models import Product


def cart_products(request):
    """
    Show the numbers of items in cart in all pages if user are log in
    """
    cart = request.session.get('cart',{})
    cart_items = []
    total = 0
    number_of_items = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        number_of_items += quantity
    return {'cart_items': cart_items, 'total': total, 'number_of_items': number_of_items}  