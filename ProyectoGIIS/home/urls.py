from turtle import home
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('carlist/', views.home, name = 'carslist'),
    path('bitacora/',views.bitacora ,name='Bitacora'),
    path('blog/', views.blog,),
]