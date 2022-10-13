""" Forms used in this app"""
from django import forms
from .models import Subscribers, Newsletter, NewsArticle

class SubscribersForm(forms.ModelForm):
    """ Subscribers form """
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))    
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

class NewsArticleForm(forms.ModelForm):
    """ News Article form """
    class Meta:
        """ Form settings """
        model = NewsArticle
        fields = '__all__'
