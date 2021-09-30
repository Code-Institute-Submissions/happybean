from django.contrib import admin
from django.urls import path
from . import views

from .views import contactView, successView


urlpatterns = [
    path('our_story', views.our_story, name='our_story'),
    path('faq', views.faq, name='faq'),
    path('contact_us', contactView, name='contact_us'),
    path('success/', successView, name='success'),
]
