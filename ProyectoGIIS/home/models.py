from django.db import models
from flask import Flask, jsonify



class Documentos(models.Model):
    
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    documento = models.FileField(upload_to='bitacoras/', )

    def __str__(self):
        return self.title



class User:
    
    def signup (self):
        user = {
            "_id" : "",
            "name": "",
            "email":"",
            "password":""

        }

        return jsonify(User), 200

    
    