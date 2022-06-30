""" Urls in this project """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_store, name='store'),
    path('<store_id>', views.store_details, name='store_details'),
    path('bag/', views.get_bag, name='bag'),
    path('greeting/', views.get_greeting, name='greeting'),
    path('order/<order_id>', views.view_order, name='order'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
]