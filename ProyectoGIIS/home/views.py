from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
import pymongo

def home(request):
    return render (request, 'home.html')


def bitacora(request):
    return render(request,"bitacora.html")


def carslist(request):
    return render(request, 'templates/carslist.html')



def blog(request):
    return render(request,"bitacora.html")
# Create your views here.
