from django.shortcuts import render, get_object_or_404
import requests
from .models import Product, Category

bag = []

# Create your views here.
def get_store(request):
    """A view to show all product"""
    
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)

def store_details(request, store_id ):
    """A view to show product details"""
    global bag
    if request.POST:
        bag.append(store_id)
    product = get_object_or_404(Product, pk=store_id)
    context = {
        'product': product,
        'bag': bag,
    }

    return render(request, 'store/store_details.html', context)

def get_bag(request):
    """A view to show the cart/bag"""
    global bag
    products = []
    grand_total = 0
    for id in bag:
        product=get_object_or_404(Product, pk=id)
        products.append(product)
        grand_total+=product.price
    
    context = {
        'products': products,
        'grand_total': grand_total,
    }

    return render(request, 'store/bag.html', context)