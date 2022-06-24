from django.test import TestCase
from home.models import Subscribers, Newsletter
from home.forms import SubscribersForm, NewsletterForm
from home.views import get_home
from django.utils import timezone as tz
from django.shortcuts import reverse


# Models test
class SubscriberTest(TestCase):

    def create_subscriber(self, email="test@test.test", date=tz.now(), subscribed=False):
        return Subscribers.objects.create(email=email, date=date, subscribed=subscribed)
    
    def test_subscriber_creation(self):
        s = self.create_subscriber()
        self.assertTrue(isinstance(s, Subscribers))
        self.assertEqual(s.__str__(), s.email)

    # Views tests

    def test_subscriber_view(self):
        s = self.create_subscriber()
        url = reverse("home.views.get_home")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


class NewsletterTest(TestCase):

    def create_newsletter(self, title="Test newsletter", message="Some random text here"):
        return Newsletter.objects.create(title=title, message=message)
    
    def test_newsletter(self):
        n = self.create_newsletter()
        self.assertTrue(isinstance(n, Newsletter))
        self.assertEqual(n.__str__(), n.title)




