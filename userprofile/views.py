from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
import requests
from store.models import Product, Category, Order

# Create your views here.

def user_profile(request):
    """ A view to show the orders of the current user """
    orders = get_list_or_404(Order, user_id=request.user.username)
    products_all = get_list_or_404(Product)
    orders_detail = []

    #Convert the order_id of each order to a list of product id's/sku to render the products of each order in the template
    for index, order in enumerate(orders):
        order.order_id = order.order_id.split(" ")
        print("products for order id ", order.order_id)
        orders_detail.append("order"+str(index))
        for product_id in order.order_id:
            product_order = get_object_or_404(Product, pk=product_id)
            print(product_order.name, 'type', type(product_order))
            orders_detail.append(product_order)
            print(orders_detail)

    context = {
        'orders': orders,
        'orders_detail': orders_detail,
      
    }
    return render(request, 'userprofile/userprofile.html', context)


