from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_store, name='store'),
    path('<store_id>', views.store_details, name='store_details'),
]