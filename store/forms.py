from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    order_id = forms.CharField(label='order_id', widget=forms.TextInput(attrs={
        'class': 'order_id',
        'placeholder': 'order_id',
        'type': 'hidden',
        'value': ''
    }))
    user_id = forms.CharField(label='user_id', widget=forms.TextInput(attrs={
        'class': 'user_id',
        'placeholder': 'user_id',
        'type': 'hidden',
        'value': ''
    }))
    grand_total = forms.IntegerField(label='grand_total', widget=forms.NumberInput(attrs={
        'class': 'grand_total',
        'placeholder': 'grand total',
        'type': 'hidden',
        'value': ''
    }))

    class Meta:
        model = Order
        fields = [
            'order_id',
            'user_id',
            'grand_total'
        ]