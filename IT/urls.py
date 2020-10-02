from django.contrib import admin
from django.urls import path
from django.urls import include, path
from IT import views

urlpatterns = [
    path('', views.scraping, name='IT'),
    path('scraping/', views.scraping, name='IT_scraping'),
    path('management/', views.management, name='IT_management'),
]
