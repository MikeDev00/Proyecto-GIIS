from django.db import models
from django.conf import settings
from djongo.storage import GridFSStorage

grid_fs_storage = GridFSStorage(collection='file_storage')

class File(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    documento = models.FileField(upload_to='bitacoras/')

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

    def __str__(self) -> str:
        return self.title
    