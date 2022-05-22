from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import requests
from store.models import Bag
from store.views import get_session_user
from .forms import SubscribersForm, Subscribers, NewsletterForm

# Create your views here.
def get_home(request):

    #Delete bag in database if it exists for the session user.
    try:
        session_user = get_session_user(request)
        bag = get_object_or_404(Bag, bag_name=session_user)
        print('bag deleted: ', bag.bag_name)
        bag.delete()
    except:
        print('bag dont exist')

    #Handle subscribers..
    if request.POST:
        form = SubscribersForm(request.POST)
        if form.is_valid():
            #Check if already subscribed
            try: 
                get_object_or_404(Subscribers, email=request.POST.get('email'))
                messages.error(request, 'Already subscribed')
            except:
                form.save()
                messages.success(request, 'You are subscribed!')
            return redirect('home')

    else:
        form = SubscribersForm()

    context = {
        'form': form,
    }

    return render(request, 'home/home.html', context)

def newsletter_create(request):
    """A view to create newsletters for admin users only"""

    if request.POST:
        nform = NewsletterForm(request.POST)
        if nform.is_valid():
            nform.save()
            messages.success(request, 'Newsletter successfully sent!')
            return redirect('newsletter_create')
    else:
        nform = NewsletterForm()
    
    context = {
        'nform': nform,
    }

    return render(request, 'home/newsletter_create.html', context)
