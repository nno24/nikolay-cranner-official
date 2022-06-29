from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
import requests
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django_pandas.io import read_frame
from store.models import Bag
from store.views import get_session_user
from .forms import SubscribersForm, Subscribers, NewsletterForm
from django.contrib.admin.views.decorators import staff_member_required
from django.templatetags.static import static


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
            #Check if already user already exist and is/not subscribed.
            try: 
                subscriber = get_object_or_404(Subscribers, email=request.POST.get('email'))
                if subscriber.subscribed:
                    messages.warning(request, 'Already subscribed')
                else:
                    subscriber.subscribed = True
                    subscriber.save()
                    messages.success(request, 'Welcome back! You are subscribed!')
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
            receipients = Subscribers.objects.filter(subscribed=True)
            df = read_frame(receipients, fieldnames=['email'])
            receipients_lst = df['email'].values.tolist()
            print(receipients_lst)

            # Render message and title into the html template
            # Also render the id of the subscriber to the template, for unsubscribe link.
            title = nform.cleaned_data.get('title')
            message = nform.cleaned_data.get('message')

            for receipient in receipients:
                print(type(receipient.email))
                newsletter_html = get_template("newsletter/one.html").render({
                    'message': message,
                    'title': title,
                    'receipient': receipient,
                })                
                mail = EmailMultiAlternatives(subject=title, from_email='', to=list(receipient.email.split(" ")))
                mail.attach_alternative(newsletter_html, 'text/html')
                mail.send()
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

def unsubscribe(request, id):
    """A view to unsubscribe"""
    try:
        subscribers = Subscribers.objects.all()
        subscriber = Subscribers.objects.get(id=id)       
        subscriber.subscribed = False
        subscriber.save()
        messages.success(request, "Successfully unsubscribed: "+ subscriber.email)

        context = {
            'subscriber': subscriber,
        }
        
    except:
        messages.error(request, "Someting went wrong..")

        context = {
            
        }        

    return render(request, 'home/unsubscribe.html', context)

def page_not_found(request, exception=None):
    """ A view to return 404 """
    return render(request, 'home/404.html', status=404)


def server_error(request, exception=None):
    """ A view to return 500 """
    return render(request, 'home/500.html', status=500)