from django.urls import path, include
from . import views
from django.contrib.admin.views.decorators import staff_member_required

# Restrict newsletter creation only for staff
views.newsletter_create = staff_member_required(views.newsletter_create, login_url='views.page_not_found')

urlpatterns = [
    path('', views.get_home, name='home'),
    path('newsletter_create/', views.newsletter_create, name='newsletter_create'),
]