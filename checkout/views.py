from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from .models import ProductOrdered
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe 


# Importing stripe api key from settings.py
stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            # get an instance of the order, (commit=false) prevents overwritting to the database
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            # request the items in the card
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                product_ordered = ProductOrdered(order = order, product = product, quantity = quantity)
                product_ordered.save()
                # Creating a charge object as per stripe instuctions to charge the constumer credit card
            try:
                costumer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id']
                    
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined!" )
            if costumer.paid:
                messages.error(request, "Thanks for your payment!")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Please check your details and try again.")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take payment with this card, Please use another card!")
    else:
        payment_form = PaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})