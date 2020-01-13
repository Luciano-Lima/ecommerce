from django import forms
from .models import Order


# Checkout Payment form 
class PaymentForm(forms.Form):
    MONTH = [(i, i) for i in range(1, 12)]
    YEAR = [(i, i) for i in range(2020, 2025)]

    cc_number = forms.CharField(label='Card Number', required=False)
    cc_cvv= forms.CharField(label='Cvv', required=False)
    cc_exp_month = forms.Select(label='Expire Month', choices=MONTH, required=False)
    cc_exp_year = forms.Select(label='Expire Year', choices=YEAR, required=False)
    strip_id =  forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    model = Order
    fields = ('first_name', 'last_name', 'address', 'city', 'post_code', 'email', 'country', 'date')