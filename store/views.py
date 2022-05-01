from django.shortcuts import render
import requests

# Create your views here.
def get_store(request):
    return render(request, 'store/store.html')
