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
    place= models.CharField('Lugar',max_length=100, blank=True, null = True)
    operator= models.CharField('Operador',max_length=100, blank=True, null = True)
    latitude= models.FloatField('Latitud',max_length=100)
    longitude= models.FloatField('Longitud',max_length=100)
    altitude= models.FloatField('Altitud',max_length=100)
    statype =  models.CharField('Tipo de Estación',max_length=100, blank=True, null = True)
    senstype = models.CharField('Tipo de Sensor',max_length=100, blank=True, null = True)
    statnum  = models.CharField('# de Estación',max_length=100, blank=True, null = True)
    sensnum = models.CharField('# de Sensor',max_length=100, blank=True, null = True)
    flname  = models.CharField('Nombre de Archivo',max_length=100, blank=True, null = True)
    freq = models.FloatField(max_length=100)
    duration  = models.FloatField(max_length=100)
    windopts  = models.CharField(max_length=100, blank=True, null = True)
    rainopts = models.CharField(max_length=100, blank=True, null = True)
    temp = models.FloatField('Temperatura',max_length=100)
    remarkstemp = models.CharField(max_length=100, blank=True, null = True)
    groundtyp = models.CharField('Tipo de Suelo',max_length=100, blank=True, null = True)
    remarksgro = models.CharField(max_length=100, blank=True, null = True)
    observations = models.TextField('Observaciones',max_length=100, blank=True, null = True)
    is_completed = models.BooleanField('Revisado',default=False)
    revisado= models.CharField('Revisado por',max_length=100, blank=True, null = True)
    nombre = models.CharField(max_length=100, blank=True, null = True)
    autor = models.CharField(max_length=100, blank=True, null = True)
    documento = models.FileField( upload_to='bitacora/', blank=True, null = False)

    def __str__(self) -> str:
        return self.documento

"""class ListaDocumentos(models.Model):
    documentos = models.ArrayField(
        model_container= PruebaBit
    )
"""

   
    