from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.coffee_corner, name='coffee_corner'),
]