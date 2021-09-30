from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum, name='forum'),
    path('add_thread', views.add_thread, name='add_thread'),
]
