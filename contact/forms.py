""" Forms used in this app"""
from django import forms
from .models import UserMessage

class UserMessageForm(forms.ModelForm):
    """ Contact form """
    class Meta:
        """ Form settings """
        model = UserMessage
        fields = '__all__'
    field_order = ['email', 'name', 'topic', 'message']
