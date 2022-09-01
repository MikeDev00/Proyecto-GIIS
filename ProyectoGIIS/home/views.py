from multiprocessing import context
from pyexpat import model
from tkinter import Grid
from warnings import filters
from django.shortcuts import render, redirect
from django.apps import apps
import pymongo
import gridfs


from flask import Flask
from .models import User
from .models import BitacoraInfo

from .forms import BitacoraForm
from .filters  import SnippetFilter




def connectDB():
    datosBitacora = pymongo.MongoClient("mongodb+srv://admin:1234@proyecto.hxkzzt7.mongodb.net/?retryWrites=true&w=majority")
    giisDB = datosBitacora.GIIS
    return giisDB

def home(request):
    return render (request, 'home.html')

def prueba(ListView):
    model= BitacoraInfo
    template_name ='prueba.html'
    
  





def datos(request):
   
    datosbita = []
    myDB = connectDB()
    bitacora = myDB["Bitacora"]
    
    for bita in bitacora.find():
        datosbita.append({ "fecha": bita["Fecha"],"place": bita["Lugar"], "operator": bita["Operador"], "statnum":bita["Statnum"]})
    return render(request, 'datos.html', {'datosbita':datosbita})



def bitacora(request):
    context = {}
    if request.method == 'GET':
        return render(request,'bitacora.html', {'bita':{}})
    if request.method == 'POST':
        form = BitacoraForm(request.POST or None, request.FILES)
        myDB = connectDB()
        fs = gridfs.GridFS(myDB)
        
        if form.is_valid():
            fecha = form.cleaned_data.get("fecha")
            hour = form.cleaned_data.get("hour")
            place = form.cleaned_data.get("place")
            operator = form.cleaned_data.get("operator")
            latitude = form.cleaned_data.get("latitude")
            longitude = form.cleaned_data.get("longitude")
            altitude = form.cleaned_data.get("altitude")
            statype = form.cleaned_data.get("statype")
            senstype = form.cleaned_data.get("senstype")
            statnum = form.cleaned_data.get("statnum")
            sensnum = form.cleaned_data.get("sensnum")
            flname = form.cleaned_data.get("flname")
            freq  = form.cleaned_data.get("freq")
            duration  = form.cleaned_data.get("duration")
            windopts = form.cleaned_data.get("windopts")
            rainopts = form.cleaned_data.get("rainopts")
            temp = form.cleaned_data.get("temp")
            remarkstemp = form.cleaned_data.get("remarkstemp")
            groundtyp = form.cleaned_data.get("groundtyp")
            remarksgro = form.cleaned_data.get("remarksgro")
            observations = form.cleaned_data.get("observations")
           

        
        bitacora = myDB["Bitacora"]
        bitacora.insert_one( { "Fecha": fecha ,"Hora": hour, "Lugar": place, "Operador": operator, "Latitud": latitude, "Longitud": longitude, 
        "Altitud": altitude, "Statype": statype, "Senstype": senstype, "Statnum": statnum, "Sensnum": sensnum, "FlName": flname, "Freq" : freq,
        "Duration": duration, "WindOpts": windopts, "RainOpts":rainopts, "Temp":temp, "RemarksTemp":remarkstemp, "GroundType": groundtyp,
        "RemarksGround": remarksgro, "Observations": observations } )
        return redirect('datos')
        

def handle_uploaded_file(f):  
    with open('C:/Users/yexil/Environments/Proyecto GIIS/ProyectoGIIS/staticfiles/upload ' + f.name, 'wb+') as destination:  
        
        for chunk in f.chunks():  
            destination.write(chunk)




def aboutus(request):
    return render(request,"aboutus.html")

def maps(request):
    return render(request,"maps.html")


def login(request):
    return render(request,"login.html")

def signup ():
    return User().signup()


