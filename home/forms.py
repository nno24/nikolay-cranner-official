""" Forms used in this app"""
from django import forms
from .models import Subscribers, Newsletter

class SubscribersForm(forms.ModelForm):
    """ Subscribers form """
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
