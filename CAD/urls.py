from django.urls import path
from CAD import views

urlpatterns = [
    path('', views.lang, name='CAD'),
    path('lang/', views.lang, name='CAD_LANG'),
    path('tol/', views.tol, name='CAD_TOL'),
    path('grp/', views.grp, name='CAD_GRP'),
    path('tool/', views.tool, name='CAD_TOOL'),
]
