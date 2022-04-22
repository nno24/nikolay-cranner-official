from django.shortcuts import render
import requests

# Create your views here.
def get_home(request):
    return render(request, 'home/home.html')
