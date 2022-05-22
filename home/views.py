from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import requests
from django.core.mail import send_mail
from django_pandas.io import read_frame
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
            #get the list of subscribers and prep message
            receipients = Subscribers.objects.all()
            df = read_frame(receipients, fieldnames=['email'])
            receipients_lst = df['email'].values.tolist()
            print(receipients_lst)

            #set title and message, and send email
            title = nform.cleaned_data.get('title')
            message = nform.cleaned_data.get('message')
            send_mail(title, message, '', receipients_lst, fail_silently=False,)
            messages.success(request, 'Newsletter successfully sent to: ')

            context = {
                'receipients_lst': receipients_lst,
            }
            return render(request, 'home/newsletter_create.html', context)
    else:
        nform = NewsletterForm()
    
    context = {
        'nform': nform,
    }

    return render(request, 'home/newsletter_create.html', context)
