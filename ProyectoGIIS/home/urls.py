from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#app_name = 'aplication'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('datos/',views.datos, name='datos'),
    path('aboutus/', views.aboutus,name='AboutUs'),
    path('Mapa/', views.maps,name='Maps'),
    path('login/', views.login_user,name='login'),
    path('Bitacora/', views.pruebabit,name='pruebabit'),
    path("logout/", views.Logout, name="logout"),





    #URL dinamicas 
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^filterbit/$', views.filterbit, name='filterbit'),


    # URL Con objetos ID para identificar elementos 
    path('editar_<int:id>/', views.editar, name= 'editar'),
    path('editar2_<int:id>/', views.editar2, name= 'editar2'),
    path('eliminar_<int:id>/', views.eliminar, name= 'eliminar')

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)