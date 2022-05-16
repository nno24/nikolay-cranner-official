from django.shortcuts import render, get_object_or_404, redirect
import requests
from store.models import Product, Category, Order

# Create your views here.

def user_profile(request):
    """ A view to show the orders of the current user """

    orders = '10 11'
    context = {
        'orders': orders,
    }
    return render(request, 'userprofile/userprofile.html', context)


