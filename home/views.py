from django.shortcuts import render, get_object_or_404
import requests
from store.views import bag
from store.models import Bag

# Create your views here.
def get_home(request):
    global bag

    #Delete bag in database if it exists for the session user.
    try:
        session_user = request.user.username
        bag_items = get_object_or_404(Bag, bag_name=session_user)
        print('bag deleted: ', bag_items)
        bag_items.delete()
    except:
        print('bag dont exist')
    bag = []

    return render(request, 'home/home.html')
