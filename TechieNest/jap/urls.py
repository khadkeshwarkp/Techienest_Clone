from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.register, name = 'register'),
]