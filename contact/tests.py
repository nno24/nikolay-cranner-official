from django.test import TestCase
from contact.forms import UserMessageForm
from contact.models import UserMessage, UserMessageOwner, UserMessageOwnerGroup



# Models test
class UserMessageTest(TestCase):

    def create_usermessage_owner(self, email="test@test1.test"):
        return UserMessageOwner.objects.create(email=email)
    
    def create_usermessage_owner_group(self, emails=None):
        return UserMessageOwnerGroup.objects.create()
    
    def create_usermessage(self, email='testuser@test.test', topic="Booking", message='this is a test message',\
                           name='John Doe', newsletter_signup=True):

        umsg = UserMessage.objects.create(email=email, topic=topic, message=message, name=name,\
                                          newsletter_signup=newsletter_signup)

        form_data = {'email':umsg.email, 'topic':umsg.topic, 'message':umsg.message, 'name':umsg.name,\
                        'newsletter_signup':umsg.newsletter_signup,}

        form = UserMessageForm(data=form_data)
        return form


    def test_usermessage_creation(self):
        # 1: Create user message owner
        umo = self.create_usermessage_owner()
        self.assertTrue(isinstance(umo, UserMessageOwner))
        self.assertEqual(umo.__str__(), umo.email)
        # 2: Create user message owner group
        umog = self.create_usermessage_owner_group(emails=umo)
        self.assertTrue(isinstance(umog, UserMessageOwnerGroup))
        self.assertEqual(umog.__str__(), umog.name)
        # 3: Validate usermessage form
        um_form = self.create_usermessage()
        self.assertTrue(um_form.is_valid())


# View tests with selenium
import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_options = Options()
firefox_options.add_argument("--headless")

class TestUserMessage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox( executable_path=GeckoDriverManager().install(), options=firefox_options )
    
    def test_usermessage_fire(self):
        self.driver.get("http://127.0.0.1:8000/contact")
        self.driver.find_element(By.ID, "id_email").send_keys("test@test1.test")
        self.driver.find_element(By.ID, "id_name").send_keys("John Doe")
        self.driver.find_element(By.ID, "id_message").send_keys("This is a test message")
        self.driver.find_element(By.ID, "id_newsletter_signup").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)
    
    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()



