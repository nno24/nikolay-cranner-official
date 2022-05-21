from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Product, Category, Bag, Order
from .forms import OrderForm
import datetime

#Global tmp variables for bag/orders
bag_counter = 0
grand_total = 0
order_id=''
session_user='guest'


def get_session_user(request):
    if request.user.is_authenticated:
        session_user = request.user.username
        print("session user is: ", session_user)
        return session_user
    else:
        session_user = 'guest'
        print("session user is: ", session_user)
        return session_user

# Create your views here.
def get_store(request):
    """A view to show all product"""
    global session_user
    #Create a bag for the user if it don't exist
    session_user = get_session_user(request)

    try:   
        bag = get_object_or_404(Bag, bag_name=session_user)
    except:
        bag = Bag(bag_name=session_user)
        bag.save()

    quantity = bag.bag_quantity
    products = Product.objects.all()
    context = {
        'products': products,
        'quantity': quantity,
    }
    return render(request, 'store/store.html', context)


def store_details(request, store_id ):
    """A view to show product details"""
    global session_user
    session_user = get_session_user(request)
    bag = get_object_or_404(Bag, bag_name=session_user)

    if request.POST:
        for key, value in request.POST.items():
            print('Key: %s' % (key))
            print('value: %s' % (value))
        
        try:
            bag.bag_items+=store_id + " "
            bag.bag_quantity+=1
        except:
            bag.bag_items=store_id + " "
            bag.bag_quantity+=1

        bag.save()

        return redirect('/store')
        

    
    quantity = bag.bag_quantity
    product = get_object_or_404(Product, pk=store_id)

    context = {
        'product': product,
        'quantity': quantity,

    }

    return render(request, 'store/store_details.html', context)



def get_bag(request):
    """A view to show the cart/bag"""
    #Global vars
    global grand_total
    global order_id
    global session_user

    #Local vars
    session_user = get_session_user(request)
    products_bag = []
    grand_total = 0
    transaction_date = datetime.date.today()
    transaction_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    print(transaction_date, transaction_time)
    bag = get_object_or_404(Bag, bag_name=session_user)

    if bag.bag_items:
        bag_items_to_list = bag.bag_items.split(" ")
    
    
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()

        form = OrderForm()


    if request.POST:
        for key, value in request.POST.items():
            print('Key: %s' % (key))
            print('value: %s' % (value))

            #If deleting an item - pop out the list item, and convert back to string / model.
            if key == 'delete' and len(bag.bag_items) != 0:
                del bag_items_to_list[int(value)]
                bag.bag_items = ' '.join(map(str, bag_items_to_list))
                bag.bag_quantity-=1
                bag.save()

                return redirect('/store/bag/')
            elif key in 'order_id':
                return redirect('greeting')

               
    #Update the products in bag view
    try: 
        bag.bag_items.split(" ")
        bag_items_to_list = bag.bag_items.split(" ")
        for id in bag_items_to_list:
            if id != "":
                product=get_object_or_404(Product, pk=id)
                products_bag.append(product)
                grand_total+=product.price
    except:
        print("no items in bag")
        quantity = bag.bag_quantity
        context = {
            'quantity': quantity,
            'grand_total': grand_total,
        }
        return render(request, 'store/bag.html', context)
    
    #Update the order form values
    order_items = bag.bag_items
    order_id = str(transaction_date) + '.' + str(transaction_time)
    quantity = bag.bag_quantity

    context = {
        'products_bag': products_bag,
        'grand_total': grand_total,
        'form': form,
        'order_id': order_id,
        'order_items': order_items,
        'transaction_date': transaction_date,
        'transaction_time': transaction_time,
        'quantity': quantity,
    }

    return render(request, 'store/bag.html', context)

def get_greeting(request):
    """A view to display success message after purchase"""
    global session_user
    session_user = get_session_user(request)
    try:   
        bag = get_object_or_404(Bag, bag_name=session_user)
        bag.delete()
        print("deleted shopping bag for: ", session_user)
        order = get_object_or_404(Order, user_id=session_user, order_id=order_id)
    except:
        return render(request, 'store/greeting.html')    
    context = {
        'order': order,
    }
    return render(request, 'store/greeting.html', context)



def view_order(request, order_id):
    """ A view to display an order """
    global session_user
    session_user = get_session_user(request)
    products_order = []

    print("the order_id is: ", order_id) 
    try:
        order = get_object_or_404(Order, user_id=session_user, order_id=order_id)
    except:
        return render(request, 'store/view_order.html')

    for id in order.order_items.split(" "):
        if id != "":
            product = get_object_or_404(Product, pk=id)
            products_order.append(product)

    context = {
        'order': order,
        'products_order': products_order,
    }
    return render(request, 'store/view_order.html', context)


def payment_failed(request):
    """ A view to  tell the user the payment failed """
    context = {

    }
    return render(request, 'store/payment_failed.html')