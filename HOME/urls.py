from django.contrib import admin
from django.urls import path
from django.urls import include, path
from HOME import views

urlpatterns = [
    path('', views.index, name='home')
]
