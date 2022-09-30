from unicodedata import name
from django.db import models
from flask import Flask, jsonify
from djongo import models


class Documentos(models.Model):
    
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    documento = models.FileField(upload_to='bitacoras/', )

    def __str__(self):
        return self.nombre


class PruebaBit(models.Model):
 
    fecha= models.CharField('Fecha', max_length=100, blank=True, null= True)
    hour= models.CharField('Hora', max_length=100, blank=True, null = True)
    place= models.CharField( max_length=100, blank=True, null = True)
    operator= models.CharField('Operador',max_length=100, blank=True, null = True)
    latitude= models.FloatField('Latitud',max_length=100, blank=True, null = True)
    longitude= models.FloatField('Longitud',max_length=100, blank=True, null = True)
    altitude= models.FloatField('Altitud',max_length=100, blank=True, null = True)
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
    
    Prueba =models.CharField('Clima',max_length=100, blank=True, null = True)
    clima= models.CharField('Clima',max_length=100, blank=True, null = True)
    Estruc= models.CharField('Estructura',max_length=100, blank=True, null = True)
    Traf= models.CharField('Trafico',max_length=100, blank=True, null = True)




    #documento = models.FileField( upload_to='bitacora/', blank=True, null = False,)
    #infinitos = models.ForeignKey(Infinitos, on_delete=models.CASCADE)


    documento = models.FileField( upload_to='bitacora/', blank=True, null = False)


    def __str__(self) -> str:
        return self.documento

   
class Infinitos(models.Model):
    medtype = models.CharField(max_length=100, blank=True, null = True)
    medicion = models.FloatField(max_length=100, blank=True, null = True)
    unidad = models.CharField(max_length=100, blank=True, null = True)
    
    def __str__(self) -> str:
        return self.medtype



class Graficos(models.Model):
    xarch = models.FileField( upload_to='bitacora/', blank=True, null = False,)
    yarch = models.FileField( upload_to='bitacora/', blank=True, null = False,)
    zarch = models.FileField( upload_to='bitacora/', blank=True, null = False,)
    nomx =  models.CharField('Nombre de Archivo',max_length=100, blank=True, null = True)
    nomy =  models.CharField('Nombre de Archivo',max_length=100, blank=True, null = True)
    nomz =  models.CharField('Nombre de Archivo',max_length=100, blank=True, null = True)

    def __str__(self) -> str:
        return self.xarch

    def __str__(self) -> str:
        return self.yarch

    def __str__(self) -> str:
        return self.zarch
    
    def __str__(self) -> str:
        return self.nomx
    
    def __str__(self) -> str:
        return self.nomy
    
    def __str__(self) -> str:
        return self.nomz

