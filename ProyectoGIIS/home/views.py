from collections import UserList
from gettext import find
from multiprocessing import context
from pydoc import Doc
from pyexpat import model
from warnings import filters
from django.shortcuts import render, redirect
from django.apps import apps
import pymongo
from django.core.files.storage import FileSystemStorage

from home.filters import UserFilter

from home.models import Documentos, User, BitacoraInfo


from .forms import BitacoraForm, DocumentoForm







def connectDB():
    datosBitacora = pymongo.MongoClient("mongodb+srv://admin:1234@proyecto.hxkzzt7.mongodb.net/?retryWrites=true&w=majority")
    giisDB = datosBitacora.GIIS
    return giisDB

def home(request):
    return render (request, 'home.html')


def prueba(request):
  datosbita = []
  myDB = connectDB()
  bitacora = myDB["Bitacora"]
    
  for bita in bitacora.find():
        datosbita.append({ "fecha": bita["Fecha"],"place": bita["Lugar"], "operator": bita["Operador"], "statnum":bita["Statnum"],
        "groundtyp": bita["GroundType"], "freq" : bita ["Freq"],"duration": bita["Duration"] })
  return render(request, 'prueba.html', {'datosbita':datosbita})
    


def search (request):
    user_list = Documentos.objects.all()
    user_filter = UserFilter(request.GET, queryset= user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

    





def datos(request):
   
    datosbita = []
    myDB = connectDB()
    bitacora = myDB["Bitacora"]
        
    for bita in bitacora.find():
        datosbita.append({ "fecha": bita["Fecha"],"place": bita["Lugar"], "operator": bita["Operador"], "statnum":bita["Statnum"]})
    return render(request, 'datos.html', {'datosbita':datosbita})




def bitacora(request):
    if request.method == 'GET':
        return render(request,'bitacora.html', {'bita':{}})
    if request.method == 'POST':
        form = BitacoraForm(request.POST or None, request.FILES)
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
            form.save()
            #fs = FileSystemStorage()
            #name = fs.save(upload_file.name, upload_file)
            #context['url'] = fs.url(name)
        myDB = connectDB()
        bitacora = myDB["Bitacora"]
        bitacora.insert_one( { "Fecha": fecha ,"Hora": hour, "Lugar": place, "Operador": operator, "Latitud": latitude, "Longitud": longitude, 
        "Altitud": altitude, "Statype": statype, "Senstype": senstype, "Statnum": statnum, "Sensnum": sensnum, "FlName": flname, "Freq" : freq,
        "Duration": duration, "WindOpts": windopts, "RainOpts":rainopts, "Temp":temp, "RemarksTemp":remarkstemp, "GroundType": groundtyp,
        "RemarksGround": remarksgro, "Observations": observations } )
        
    return render(request, 'bitacora.html')

def bitacora(request):
    if request.method =='POST':
        docform = DocumentoForm(request.POST, request.FILES)
        if docform.is_valid():
            docform.save()
            return redirect('datos')
    else:
        docform = DocumentoForm()
    return render(request, 'bitacora.html',  {
            'docform': docform
    })
        
        




def aboutus(request):
    return render(request,"aboutus.html")

def maps(request):
    return render(request,"maps.html")




def login(request):
    return render(request,"login.html")

def signup ():
    return User().signup()



