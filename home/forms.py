""" Forms used in this app"""
from django import forms
from .models import Subscribers, Newsletter

class SubscribersForm(forms.ModelForm):
    """ Subscribers form """
    email = forms.EmailField(label='Become an insider..')
    email.widget.attrs.update({'placeholder': 'Email'})
    class Meta:
        """ Form settings """
        model = Subscribers
        fields = ['email',]

class NewsletterForm(forms.ModelForm):
    """ Newsletter form """
    class Meta:
        """ Form settings """
        model = Newsletter
        fields = '__all__'
