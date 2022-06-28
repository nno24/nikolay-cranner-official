from django.contrib import admin
from .models import UserMessage, UserMessageOwner,\
                    UserMessageOwnerGroup

# Register your models here.
admin.site.register(UserMessage)
admin.site.register(UserMessageOwner)
admin.site.register(UserMessageOwnerGroup)