from turtle import home
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('bitacora/',views.bitacora ,name='bitacora'),
    path('datos/',views.datos, name='datos'),
    path('aboutus/', views.aboutus,name='AboutUs'),
    path('maps/', views.maps,name='Maps'),
    path('prueba/', views.prueba,name='prueba'),
    path('login/', views.login,name='login'),
]