from copyreg import pickle
from importlib.resources import path
from multiprocessing import context
from pathlib import Path
from posixpath import dirname
from pydoc import doc, resolve
import shutil
from django.shortcuts import render, redirect, get_object_or_404
import pymongo
from home.models import PruebaBit
import zipfile
import os

from home.filters import UserFilter, BitFilter


from .forms import BitacoraForm, PruebaBitaForm


# conector con la base de datos MongoDb
def connectDB():
    datosBitacora = pymongo.MongoClient("mongodb+srv://admin:1234@proyecto.hxkzzt7.mongodb.net/?retryWrites=true&w=majority")
    giisDB = datosBitacora.GIIS
    return giisDB


# Primera vista de plataforma 
def home(request):
    return render (request, 'home.html')


# Filtros  en  la pantalla de descarga

def search(request):
    user_list = PruebaBit.objects.all()
    user_filter = UserFilter(request.GET, queryset= user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

def filterbit (request):
    bit_filt = PruebaBit.objects.all()
    bita_filter = BitFilter(request.GET, queryset= bit_filt)
    return render(request, 'datosfilt.html', {'filter': bita_filter})


#Pagina para visualizar Datos
def datos(request):
   
    datosbita = []
    myDB = connectDB()
    bitacora = myDB["home_pruebabit"]
        
    for bita in bitacora.find():
        datosbita.append({ 
            "fecha": bita["fecha"],
            "place": bita["place"], 
            "operator": bita["operator"], 
            "latitude":bita["latitude"],
            "longitude":bita["longitude"],
            "senstype":bita["senstype"],
            "freq":bita["freq"],
            "freq2":bita["freq2"],
            "remarkstemp":bita["remarkstemp"],
            "remarksgro":bita["remarksgro"],
            })
    return render(request, 'datos.html', {'datosbita':datosbita})





        
#pagina de bitacora      
def pruebabit(request):
    if request.method =='POST':
        pruebaform = PruebaBitaForm(request.POST, request.FILES)
        documentos = request.FILES.getlist('documento')
        nombre = request.POST.get('nombre')
        if pruebaform.is_valid():
           
            with zipfile.ZipFile(f"{nombre}.zip", mode= "w") as archive:
                name = f"{nombre}.zip"
                for file in documentos:
                    with open(f'{file.name}', 'wb+') as destination:
                        for chunk in file.chunks():
                             destination.write(chunk)
                             
                        archive.write(f'{file.name}')
                   
                        
                    os.remove( f'{file.name}')   
                prueba = PruebaBit(documento= f"{nombre}.zip",
                        fecha = request.POST.get('fecha') ,
                        hour = request.POST.get('hour'),
                        place =request.POST.get('place'),
                        operator = request.POST.get('operator'),
                        latitude = request.POST.get('latitude'), 
                        longitude = request.POST.get('longitude'), 
                        altitude = request.POST.get('altitude'),
                        statype = request.POST.get('statype'), 
                        senstype = request.POST.get('senstype'), 
                        statnum = request.POST.get('statnum'), 
                        sensnum =request.POST.get('sensnum'),
                        freq = request.POST.get('freq'),
                        freq2 = request.POST.get('freq2'), 
                        duration =request.POST.get('duration'), 
                        windopts = request.POST.get('windopts'),
                        rainopts = request.POST.get('rainopts'), 
                        temp = request.POST.get('temp'), 
                        remarkstemp =request.POST.get('remarkstemp'), 
                        groundtyp = request.POST.get('groundtyp'), 
                        remarksgro = request.POST.get('remarksgro'), 
                        observations = request.POST.get('observations'), 
                        #is_completed = request.POST.get('is_completed'),
                        revisado = request.POST.get('revisado'),
                        nombre = request.POST.get('nombre'.upper), 
                        autor = request.POST.get('autor'), )
                #Path("/ProyectoGIIS/name").rename("/ProyectoGIIS/media/bitacora")
            #    pruebaform = PruebaBitaForm (request.POST, documento = f"{nombre}.zip" )
            prueba.save()
           
            global nomarch
            nomarch= (f'{nombre}')
        
            print(nomarch)

            ruta = r"./media"
            shutil.move(f'{nombre}.zip',ruta)
            
        return redirect('datos')
        
    else:
        pruebaform=PruebaBitaForm()
    return render(request, 'pruebabit.html',  {
            'pruebaform': pruebaform
    })



# pagina sobre nosotros
def aboutus(request):
    return render(request,"aboutus.html")


# pagina del mapa 
def maps(request):
    return render(request,"maps.html")


# pagina del login sin crear
def login(request):
    return render(request,"login.html")






# Accion de edicion de en los filtros
def editar(request, id):
    bit = get_object_or_404(PruebaBit, id = id)
    data  = {'pruebaform':PruebaBitaForm(instance=bit) }
    if request.method =='POST':
        pruebaform = PruebaBitaForm(request.POST, instance=bit)
        documentos = request.FILES.getlist('documento')
        nombre = request.POST.get('nombre')
        

        if pruebaform.is_valid():
        
            pruebaform.save()
            return redirect('filterbit')
    else : 
            pruebaform=PruebaBitaForm()
    return render(request, 'editar.html',data)


# Accion de edicion de en los Archivos
def editar2(request, id):
    bit = get_object_or_404(PruebaBit, id = id)
    data  = {'pruebaform':PruebaBitaForm(instance=bit) }
    if request.method =='POST':
        pruebaform = PruebaBitaForm(request.POST, request.FILES, instance=bit)
        documentos = request.FILES.getlist('documento')
        nombre = request.POST.get('nombre')
         
        if pruebaform.is_valid():
           
            #creación de archivo Zip
            with zipfile.ZipFile(f"{nombre}.zip", mode= "w") as archive:
                
              
                for file in documentos:
                    with open(f'{file.name}', 'wb+') as destination:
                        for chunk in file.chunks():
                             destination.write(chunk)
                             
                        archive.write(f'{file.name}')
                   
                        
                    os.remove( f'{file.name}')   
                prueba = PruebaBit(
                        documento= f"{nombre}.zip",
                        fecha = request.POST.get('fecha') ,
                        hour = request.POST.get('hour'),
                        place =request.POST.get('place'),
                        operator = request.POST.get('operator'),
                        latitude = request.POST.get('latitude'), 
                        longitude = request.POST.get('longitude'), 
                        altitude = request.POST.get('altitude'),
                        statype = request.POST.get('statype'), 
                        senstype = request.POST.get('senstype'), 
                        statnum = request.POST.get('statnum'), 
                        sensnum =request.POST.get('sensnum'),
                        freq = request.POST.get('freq'),
                        freq2 = request.POST.get('freq2'), 
                        duration =request.POST.get('duration'), 
                        windopts = request.POST.get('windopts'),
                        rainopts = request.POST.get('rainopts'), 
                        temp = request.POST.get('temp'), 
                        remarkstemp =request.POST.get('remarkstemp'), 
                        groundtyp = request.POST.get('groundtyp'), 
                        remarksgro = request.POST.get('remarksgro'), 
                        observations = request.POST.get('observations'), 
                        is_completed = bool(request.POST.get('is_completed')),
                        revisado = request.POST.get('revisado'),
                        nombre = request.POST.get('nombre',), 
                        autor = request.POST.get('autor'), )
                #Path("/ProyectoGIIS/name").rename("/ProyectoGIIS/media/bitacora")
            #    pruebaform = PruebaBitaForm (request.POST, documento = f"{nombre}.zip" )
            
            prueba.save()
           
            
            ruta = r"./media"
            shutil.move(f'{nombre}.zip',ruta)
            
        return redirect('filterbit')
    else : 
            pruebaform=PruebaBitaForm()
    return render(request, 'editar2.html',data)



# Acion de eliminar 
def eliminar(request, id):
    bita = get_object_or_404(PruebaBit, id = id)
    bita.delete()
    return redirect(to="filterbit")
