from django.shortcuts import render
import requests

# Create your views here.
def get_contact(request):
    return render(request, 'contact/contact.html')
