from django.contrib import admin
from django.urls import path
from django.urls import include, path
from Blog import views

urlpatterns = [
    path('', views.index, name='Blog'),
    path('detail/<int:blog_id>/', views.detail, name='blog_detail'),
]
