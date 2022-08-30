from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('bitacora/',views.bitacora ,name='bitacora'),
    path('datos/',views.datos, name='datos'),
    path('aboutus/', views.aboutus,name='AboutUs'),
    path('maps/', views.maps,name='Maps'),
    path('prueba/', views.prueba,name='prueba'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)