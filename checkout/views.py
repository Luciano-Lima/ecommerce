from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm, PaymentForm 
from .models import ProductOrdered
from products.models import Product
import stripe 

# Importing stripe api key from settings.py
stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
@login_required()
def checkout(request):
    if request.method=="POST":
        order = OrderForm(request.POST)
        payment = PaymentForm(request.POST)
        if order.is_valid() and payment.is_valid():
            # get an instance of the order, (commit=false) prevents overwritting to the database
            order = order.save(commit=False)
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
                    currency = "LBP",
                    receipt_emal = request.user.email,
                    description = "Your Payment has beed succesfully completed. You will receive an email confirmation shortly.",
                    card = payment.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "The payment has been declined, please use another card." )
            if costumer.paid:
                messages.error(request, "We have received you payment. Thanks")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Please check your detail and try again.")
        else:
            print(PaymentForm.errors)
            messages.error(request, "Your card has been declined.")
    else:
        order = OrderForm()
        payment = PaymentForm()
    return render(request, "checkout.html", {"order": order, "payment": payment, "publishable": settings.STRIPE_PUBLISHABLE})