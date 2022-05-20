from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
import requests
from store.models import Product, Category, Order
from store.views import get_session_user

# Create your views here.

def user_profile(request):
    """ A view to show the orders of the current user """
    session_user = get_session_user(request)
    orders = Order.objects.filter(user_id=session_user)
    context = {
        'session_user': session_user,
        'orders': orders,
    }

    return render(request, 'userprofile/userprofile.html', context)


