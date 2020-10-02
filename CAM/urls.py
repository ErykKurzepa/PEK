from django.contrib import admin
from django.urls import path
from django.urls import include, path
from CAM import views

urlpatterns = [
    path('', views.probe, name='CAM'),
    path('probe/', views.probe, name='CAM_probe'),
    path('measure/', views.measure, name='CAM_measure'),
    path('cnc/', views.cnc, name='CAM_cnc'),
]
