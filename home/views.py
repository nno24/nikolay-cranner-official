from django.shortcuts import render, get_object_or_404
import requests
from store.models import Bag

# Create your views here.
def get_home(request):

    #Delete bag in database if it exists for the session user.
    try:
        session_user = request.user.username
        bag = get_object_or_404(Bag, bag_name=session_user)
        print('bag deleted: ', bag.name)
        bag.delete()
    except:
        print('bag dont exist')

    return render(request, 'home/home.html')
