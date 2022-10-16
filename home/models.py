""" Database models in this app"""
from django.db import models
from django.utils import timezone as tz

# Create your models here.
class Subscribers(models.Model):
    """ Model for subscribers"""
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)

class Newsletter(models.Model):
    """ Model for newsletters"""
    title = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(null=True)

    def __str__(self):
        return str(self.title)

class NewsArticle(models.Model):
    """ Model for news article on home page """
    title = models.CharField(max_length=50, null=True, blank=True)
    section1 = models.TextField(default="", null=True, blank=True)
    section2 = models.TextField(default="", null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='articles/')
    embed = models.CharField(null=True, blank=True, max_length=500)
    media = models.FileField(null=True, blank=True, upload_to='articles/')
    live = models.BooleanField(default=False)
    pubdate = models.DateField(default=tz.now)
    showdate = models.BooleanField(default=True)