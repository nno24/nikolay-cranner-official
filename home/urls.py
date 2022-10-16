""" Urls defined for this app"""
from django.urls import path, include
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Restrict newsletter creation only for staff
views.newsletter_create = staff_member_required(views.newsletter_create, \
                                                login_url='views.page_not_found')

urlpatterns = [
    path('', views.get_home, name='home'),
    path('newsletter_create/', views.newsletter_create, name='newsletter_create'),
    path('newsarticles/', views.newsarticles, name='newsarticles'),
    path('newsarticle_preview/<article_id>', views.newsarticle_preview, name='newsarticle_preview'),
    path('newsarticle_edit/<article_id>', views.newsarticle_edit, name='newsarticle_edit'),
    path('newsarticle_delete/<article_id>', views.newsarticle_delete, name='newsarticle_delete'),
    path('newsarticle_delete_yes/<article_id>', views.newsarticle_delete_yes, name='newsarticle_delete_yes'),
    path('newsarticle_create/', views.newsarticle_create, name='newsarticle_create'),
    path('unsubscribe/<id>', views.unsubscribe, name='unsubscribe'),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
