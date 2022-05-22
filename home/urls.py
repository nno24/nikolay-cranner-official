from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('newsletter_create/', views.newsletter_create, name='newsletter_create'),
]