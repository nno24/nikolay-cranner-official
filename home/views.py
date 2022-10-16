""" View functions for this app"""
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.templatetags.static import static
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django_pandas.io import read_frame
from store.models import Bag
from store.views import get_session_user
from .models import NewsArticle
from .forms import SubscribersForm, Subscribers, NewsletterForm, \
                    NewsArticleForm

# Create your views here.
def get_home(request):
    """ A view for the home page, subscribers, etc"""
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


    # Get the news with live status to True
    try:
        newsarticles = NewsArticle.objects.filter(live=True)
    except:
        messages.warning(request, "Unable to load latest news..")
    
    context = {
        'form': form,
        'newsarticles': newsarticles,
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


def newsarticles(request):
    """ A view to display all news articles"""
    articles = NewsArticle.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'home/newsarticles.html', context)


def newsarticle_preview(request, article_id):
    """ A view to preview a news article """
    this_article = NewsArticle.objects.get(id=article_id)
    context = {
        'this_article': this_article,
    }

    return render(request, 'home/newsarticle_preview.html', context)


def newsarticle_edit(request, article_id):
    """ A view to preview a news article """

    if request.POST:
        try:
            this_article = NewsArticle.objects.get(id=article_id)
            this_form = NewsArticleForm(request.POST, request.FILES)
            if this_form.is_valid():
                # Get the form, and compare if changes with object in db, only update db if changes.
                cf = this_form.cleaned_data
                ftitle = cf['title']
                fsection1 = cf['section1']
                fsection2 = cf['section2']
                flive = cf['live']
                fimage = cf['image']
                fembed = cf['embed']
                fshowdate = cf['showdate']

                if (ftitle != this_article.title):
                    this_article.title = ftitle
                if ( fsection1 != this_article.section1 ):
                    this_article.section1 = fsection1
                if ( fsection2 != this_article.section2 ):
                    this_article.section2 = fsection2
                if ( flive != this_article.live ):
                    this_article.live = flive
                if ( fembed != this_article.embed ):
                    this_article.embed = fembed
                if ( fimage != this_article.image and fimage != None ):
                    this_article.image = fimage
                if ( fshowdate != this_article.showdate ):
                    this_article.showdate = fshowdate
                this_article.save()
                messages.success(request, "Updated")
                return redirect('newsarticles')
        except:
            messages.error(request, "Failed to update")

    this_article = NewsArticle.objects.get(id=article_id)
    this_form = NewsArticleForm(instance=this_article)
    context = {
        'this_form': this_form,
    }

    return render(request, 'home/newsarticle_edit.html', context)

def newsarticle_delete(request, article_id):
    """ A view to be asked if delete YES/NO """
    newsarticle = NewsArticle.objects.get(id=article_id)
    context = {
        'newsarticle': newsarticle,
    }
    return render(request, 'home/newsarticle_delete.html', context)

def newsarticle_delete_yes(request, article_id):
    """ Delete function """
    try:
        newsarticle = NewsArticle.objects.get(id=article_id)
        newsarticle.delete()
        messages.success(request, "Deleted: " + newsarticle.title)
    except:
        messages.error(request, "Failed to delete..")
    return redirect('newsarticles')


def newsarticle_create(request):
    """A view to create newsarticle for admin users only"""

    if request.POST:
        articleform = NewsArticleForm(request.POST, request.FILES)
        if articleform.is_valid():
            try:
                articleform.save()
                messages.success(request, "Saved")
                return redirect('newsarticles')
            except:
                messages.error(request, 'Unable to create..')
                return redirect('newsarticle_create')
            
    else:
        articleform = NewsArticleForm()
    
    context = {
        'articleform': articleform,
    }

    return render(request, 'home/newsarticle_create.html', context)

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