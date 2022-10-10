from django.urls import reverse
from email.policy import default
from unicodedata import name
from django import db
from django.db import models
from flask import Flask, jsonify
from djongo import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField 




class PruebaBit(models.Model):

    class params:
        db = 'default'
 
    fecha= models.CharField('Fecha', max_length=100, blank=True, null= True)
    hour= models.CharField('Hora', max_length=100, blank=True, null = True)
    place= models.CharField( max_length=100, blank=True, null = True)
    operator= models.CharField('Operador',max_length=100, blank=True, null = True)
    latitude= models.FloatField('Latitud',max_length=100, blank=True, null = True)
    longitude= models.FloatField('Longitud',max_length=100, null=True, blank=True, default=None)
    altitud= models.DecimalField('Altitud', null=True,blank=True, default =None, max_digits=8, decimal_places=6,)
    statype =  models.CharField('Tipo de Estación',max_length=100, blank=True, null = True)
    senstype = models.CharField('Tipo de Sensor',max_length=100, blank=True, null = True)
    statnum  = models.CharField('# de Estación',max_length=100, blank=True, null = True)
    sensnum = models.CharField('# de Sensor',max_length=100, blank=True, null = True)
    freq = models.FloatField('Frecuencia (Hz)',max_length=100, blank=True, null = True)
    freq2 = models.FloatField('Frecuencia (Hz)',max_length=100, blank=True, null = True)
    duration  = models.FloatField('Duración',max_length=100, blank=True, null = True)
    windopts  = models.CharField('Condiciones de Viento',max_length=100, blank=True, null = True)
    rainopts = models.CharField('Condiciones de Lluvia',max_length=100, blank=True, null = True)
    temp = models.FloatField('Temperatura',max_length=100, blank=True, null = True)
    remarkstemp = models.CharField('Observaciones de temperatura',max_length=100, blank=True, null = True)
    groundtyp = models.CharField('Tipo de Suelo',max_length=100, blank=True, null = True)
    remarksgro = models.CharField('Observaciones de Tierra',max_length=100, blank=True, null = True)
    observations = models.TextField('Observaciones',max_length=100, blank=True, null = True)
    is_completed = models.BooleanField('Revisado',default=False)
    revisado= models.CharField('Revisado por',max_length=100, blank=True, null = True)
    nombre = models.CharField('Nombre de Archivo',max_length=100, blank=True, null = True)
    autor = models.CharField('Autor del archivo',max_length=100, blank=True, null = True)
    medtype = models.CharField(max_length=100, blank=True, null = True)
    medicion = models.FloatField(max_length=100, blank=True, null = True)
    unidad = models.CharField(max_length=100, blank=True, null = True)
    Prueba =models.CharField('Clima',max_length=100, blank=True, null = True)
    clima= models.CharField('Clima',max_length=100, blank=True, null = True)
    Estruc= models.CharField('Estructura',max_length=100, blank=True, null = True)
    Traf= models.CharField('Trafico',max_length=100, blank=True, null = True)
    documento = models.FileField( upload_to='bitacora/', blank=True, null = False)
    
    def __str__(self) -> str:
        return self.altitude,

class Usuario(models.Model):
    class params:
        db='users'

class BlogPost(models.Model):
    title=models.CharField('Titulo',max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField("Titulo-URL",max_length=130)
    content=models.TextField("Contenido")
    prueba = RichTextField(null=True, blank=True)
    image = models.ImageField("Imagen",upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    #inv
    def get_absolute_url(self):
        return reverse('blogs')


    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    prueba = RichTextField(null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    

