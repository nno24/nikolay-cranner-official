from django.shortcuts import render
import requests
from .models import Product, Category


# Create your views here.
def get_store(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)
