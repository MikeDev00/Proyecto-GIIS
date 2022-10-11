from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#app_name = 'aplication'

urlpatterns = [

    #URL Basicos
    path('', views.home, name = 'home'),
    path('datos/',views.datos, name='datos'),
    path('aboutus/', views.aboutus,name='AboutUs'),
    path('Mapa/', views.maps,name='Maps'),
    path('login/', views.login,name='login'),
    path('Bitacora/', views.pruebabit,name='pruebabit'),

    #URL Acciones del Blog
   
    path("blog", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", views.UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),




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