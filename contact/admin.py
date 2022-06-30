""" Registered models to be shown in admin app"""
from django.contrib import admin
from .models import UserMessage, UserMessageOwner,\
                    UserMessageOwnerGroup

admin.site.register(UserMessage)
admin.site.register(UserMessageOwner)
admin.site.register(UserMessageOwnerGroup)
