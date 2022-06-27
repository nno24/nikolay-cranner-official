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


class NewsletterTest(TestCase):

    def create_newsletter(self, title="Test newsletter", message="Some random text here"):
        return Newsletter.objects.create(title=title, message=message)
    
    def test_newsletter(self):
        n = self.create_newsletter()
        self.assertTrue(isinstance(n, Newsletter))
        self.assertEqual(n.__str__(), n.title)



# View tests with selenium

import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = Options()
firefox_options.add_argument("--headless")

class TestNewsletterSignup(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver = webdriver.Firefox( executable_path=GeckoDriverManager().install(), options=firefox_options )
    
    def test_newsletter_signup_fire(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element(By.ID, "id_email").send_keys("ttt@ttt.com")
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)
    
    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()

