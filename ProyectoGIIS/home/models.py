from unicodedata import name
from django.db import models

from flask import Flask, jsonify

class User:
    
    def signup (self):
        user = {
            "_id" : "",
            "name": "",
            "email":"",
            "password":""

        }

        return jsonify(User), 200



class BitacoraInfo(models.Model):
 
    fecha= models.CharField(max_length=100)
    hour= models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    operator= models.CharField(max_length=100)
    latitude= models.FloatField(max_length=100)
    longitude= models.FloatField(max_length=100)
    altitude= models.FloatField(max_length=100)
    statype =  models.CharField(max_length=100)
    senstype = models.CharField(max_length=100)
    statnum  = models.CharField(max_length=100)
    sensnum = models.CharField(max_length=100)
    flname  = models.CharField(max_length=100)
    freq = models.FloatField(max_length=100)
    duration  = models.FloatField(max_length=100)
    windopts  = models.CharField(max_length=100)
    rainopts = models.CharField(max_length=100)
    temp = models.FloatField(max_length=100)
    remarkstemp = models.CharField(max_length=100)
    groundtyp = models.CharField(max_length=100)
    remarksgro = models.CharField(max_length=100)
    observations = models.CharField(max_length=100)
    file = models.FileField()
    



# Create your models here.
