""" Registered models to be shown in admin app"""
from django.contrib import admin
from .models import Subscribers, Newsletter

admin.site.register(Subscribers)
admin.site.register(Newsletter)
