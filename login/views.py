from django.shortcuts import render
import requests

# Create your views here.
def get_login(request):
    return render(request, 'login/login.html')
