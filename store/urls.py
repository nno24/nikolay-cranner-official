from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_store, name='store'),
    path('<store_id>', views.store_details, name='store_details'),
    path('bag/', views.get_bag, name='bag'),
    path('greeting/', views.get_greeting, name='greeting'),
    path('order/<order_id>', views.view_order, name='order'),
]