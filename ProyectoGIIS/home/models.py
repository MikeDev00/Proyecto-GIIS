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

# Create your models here.
