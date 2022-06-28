from django import forms
from .models import UserMessage

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = '__all__'
    field_order = ['email', 'name', 'topic', 'message'] 
        