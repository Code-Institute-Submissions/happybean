"""
Urls for About Pages including Our Story, FAQ & Contact Form
"""

from django.urls import path
from . import views
from .views import contact_view, success_view


urlpatterns = [
    path('our_story', views.our_story, name='our_story'),
    path('faq', views.faq, name='faq'),
    path('contact_us', contact_view, name='contact_us'),
    path('success/', success_view, name='success'),
]
