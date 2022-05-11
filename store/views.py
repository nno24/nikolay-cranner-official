from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Product, Category
from django.http import JsonResponse
from .forms import OrderForm

#Global variables for bag
bag = []
products_bag = []
grand_total = 0


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
        return redirect('store')


    product = get_object_or_404(Product, pk=store_id)
    context = {
        'product': product,
        'bag': bag,

    }

    return render(request, 'store/store_details.html', context)



def get_bag(request):
    """A view to show the cart/bag"""
    global bag
    global products_bag
    products_bag = []
    global grand_total
    grand_total = 0
    download = 'disabled'
    remove = ''
    
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()

        form = OrderForm()


    if request.POST:
        for key, value in request.POST.items():
            print('Key: %s' % (key))
            print('value: %s' % (value))

            #If deleting an item
            if key == 'delete' and len(bag) != 0:
                del bag[int(value)]
            #If order was submitted to database, after successful purchase ->
            # enable downloads disable remove buttons.
            elif key == 'order_id':
                download = ''
                remove = 'disabled'

    
    #Update the products in bag view
    for id in bag:
        product=get_object_or_404(Product, pk=id)
        products_bag.append(product)
        grand_total+=product.price
    
    context = {
        'products_bag': products_bag,
        'grand_total': grand_total,
        'form': form,
        'download': download,
        'remove': remove,
    }

    return render(request, 'store/bag.html', context)

def get_greeting(request):
    global products_bag
    global grand_total

    context = {
        'products_bag': products_bag,
        'grand_total': grand_total,
    }
    return render(request, 'store/greeting.html', context)