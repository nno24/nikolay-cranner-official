from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Product, Category
from .forms import OrderForm
import datetime

#Global variables for bag
bag = []
bag_items = 0
products_bag = []
grand_total = 0


# Create your views here.
def get_store(request):
    """A view to show all product"""
    global bag_items

    products = Product.objects.all()
    context = {
        'products': products,
        'bag_items': bag_items,
    }
    return render(request, 'store/store.html', context)


def store_details(request, store_id ):
    """A view to show product details"""
    global bag
    global bag_items


    if request.POST:
        bag.append(store_id)
        bag_items+=1
        


    product = get_object_or_404(Product, pk=store_id)
    context = {
        'product': product,
        'bag': bag,
        'bag_items': bag_items,

    }

    return render(request, 'store/store_details.html', context)



def get_bag(request):
    """A view to show the cart/bag"""
    global bag
    global products_bag
    global grand_total
    global bag_items

    products_bag = []
    grand_total = 0
    transaction_date = datetime.date.today()
    transaction_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    print(transaction_date, transaction_time)

    #download and buttons disabled status
    download = 'disabled'
    download_pointer_events = 'none'
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
                bag_items-=1
            #If order was submitted to database, after successful purchase ->
            # enable downloads disable remove buttons and set date and time
            elif key == 'order_id':
                download = ''
                remove = 'disabled'
                download_pointer_events = 'auto'
                transaction_date = datetime.date.today()
                transaction_time = datetime.datetime.now().time().strftime("%H:%M:%S")

    
    #Update the products in bag view
    for id in bag:
        product=get_object_or_404(Product, pk=id)
        products_bag.append(product)
        grand_total+=product.price
    
    #Update the order form values
    order_id =' '.join(map(str,bag))

    context = {
        'products_bag': products_bag,
        'grand_total': grand_total,
        'form': form,
        'download': download,
        'remove': remove,
        'download_pointer_events': download_pointer_events,
        'order_id': order_id,
        'transaction_date': transaction_date,
        'transaction_time': transaction_time,
        'bag_items': bag_items,
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