from django.db import models

# Create your models here.

class UserMessage(models.Model):
    TOPICS = (
        ('Booking', 'Booking'),
        ('Other', 'Other')
    )       
    email = models.EmailField(null=False, blank=False)
    topic = models.CharField(choices=TOPICS, default="Booking", null=False,\
                             blank=False, max_length=15)
    message = models.TextField(null=False, blank=False, max_length=1000)
    name = models.CharField(null=True, blank=True, max_length=30)
    newsletter_signup = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class UserMessageOwner(models.Model):
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self):
        return self.email    


class UserMessageOwnerGroup(models.Model):
    TOPICS = (
        ('Booking', 'Booking'),
        ('Other', 'Other')
    )
    name = models.CharField(choices=TOPICS, default="Booking", null=False,\
                             blank=False, max_length=15)
    emails = models.ManyToManyField(UserMessageOwner)
    
    def __str__(self):
        return self.name
