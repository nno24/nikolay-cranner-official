from django.shortcuts import render, get_object_or_404
import requests
from .models import Product, Category
from django.http import JsonResponse

#Global variables for bag
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
    products_bag = []
    grand_total = 0
    
    if request.POST:
        for key, value in request.POST.items():
            print('Key: %s' % (key))
            print('value: %s' % (value))
            if key == 'delete' and len(bag) != 0:
                del bag[int(value)]
    
    #Update the products in bag view
    for id in bag:
        product=get_object_or_404(Product, pk=id)
        products_bag.append(product)
        grand_total+=product.price
    
    context = {
        'products_bag': products_bag,
        'grand_total': grand_total,
    }

    return render(request, 'store/bag.html', context)