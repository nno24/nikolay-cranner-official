from django.shortcuts import render, get_object_or_404
import requests
from .models import Product, Category


# Create your views here.
def get_store(request):
    """A view to show all product"""
    
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)

def store_details(request, store_id):
    """A view to show product details"""

    product = get_object_or_404(Product, pk=store_id)
    context = {
        'product': product,
    }

    return render(request, 'store/store_details.html', context)