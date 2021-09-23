from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('our_story', views.our_story, name='our_story'),
    path('faq', views.faq, name='faq'),
    path('contact_us', views.contact_us, name='contact_us'),
]