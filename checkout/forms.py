from django import forms
from .models import Order


# Checkout Payment form 
class PaymentForm(forms.Form):
    MONTH = [(i, i) for i in range(1, 12)]
    YEAR = [(i, i) for i in range(2020, 2028)]

    number = forms.CharField(label='Card Number', required=False)
    cvv = forms.CharField(label='Security code (cvv)', required=False)
    exp_month = forms.ChoiceField(label='Expiry Month', choices=MONTH, required=False)
    exp_year = forms.ChoiceField(label='Expiry Year', choices=YEAR, required=False)
    stripe_id =  forms.CharField(widget=forms.HiddenInput)
    


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'address', 'city', 'post_code', 'country') 