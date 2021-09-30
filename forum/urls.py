from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum, name='forum'),
    path('add_thread', views.add_thread, name='add_thread'),
    path('thread', views.thread, name='thread'),
    path('thread/add_comment/', views.add_comment, name='add_comment'),
]
