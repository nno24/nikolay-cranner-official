from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.contrib import messages
from .forms import UserMessageForm
from .models import UserMessage, UserMessageOwnerGroup
from home.models import Subscribers
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django_pandas.io import read_frame
from nc import settings

# Create your views here.
def get_contact(request):
    """ A  view to contact the business """
    if request.POST:
        form = UserMessageForm(request.POST)
        if form.is_valid():
            receipient = form.cleaned_data.get('email')
            # If the user signed up for newsletter, add to subscribers.
            if form.cleaned_data.get('newsletter_signup') == True:
                try:
                    get_object_or_404(Subscribers, email=receipient)
                    messages.warning(request, "Already subscribed")
                except:
                    Subscribers.objects.create(email=form.cleaned_data.get('email'))
                    messages.success(request, "Successfully subscribed")
            form.save()

            # Send verification email to the user
            try:
                title = form.cleaned_data.get('topic') + " " + form.cleaned_data.get('name')
            except:
                title = form.cleaned_data.get('topic')
            message = form.cleaned_data.get('message')
            usermessage_html = get_template("usermessage/autoreply.html").render({
                'message': message,
                'title': title,
                'receipient': receipient,
            })
            mail = EmailMultiAlternatives(subject=title, from_email='', to=[receipient])
            mail.attach_alternative(usermessage_html, 'text/html')
            mail.send()
            messages.success(request, "Message successfully sent..")

            # Send email to owner
            name = form.cleaned_data.get("name")
            ownermessage_html = get_template("usermessage/ownermessage.html").render({
                'message': message,
                'title': title,
                'name': name,
            })
            try:
                # convert the list of receipients in group to list depending on topic
                receipients_group = UserMessageOwnerGroup.objects.filter(name=form.cleaned_data.get('topic'))
                receipients = []
                for owner in receipients_group:
                    for email in owner.emails.all():
                        receipients.append(email)
            except:
                receipients = [settings.DEFAULT_FROM_EMAIL]
            mail = EmailMultiAlternatives(subject=title, from_email='', to=receipients)
            mail.attach_alternative(ownermessage_html, 'text/html')
            mail.send()

            return redirect('home')
            
    form = UserMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
