from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
import pymongo

def home(request):
    return render (request, 'home.html')


def bitacora(request):
    return render(request,"bitacora.html")


def blog(request):
    return render(request,"bitacora.html")

def datos(request):
    return render(request,"datos.html")
# Create your views here.
