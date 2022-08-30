from django.shortcuts import render, redirect
from django.apps import apps
import pymongo
from django.core.files.storage import FileSystemStorage


from .forms import BitacoraForm


def connectDB():
    datosBitacora = pymongo.MongoClient("mongodb+srv://admin:1234@proyecto.hxkzzt7.mongodb.net/?retryWrites=true&w=majority")
    giisDB = datosBitacora.GIIS
    return giisDB


def home(request):
    return render (request, 'home.html')

def prueba(request):
    return render (request, 'prueba.html')


def bitacoralist(request):
    BitacoraForm = []
    myDB = connectDB()
    bitacora = myDB["Bitacora"]

    for bita in bitacora.find():
        BitacoraForm.append({ "Fecha": bita["fecha"],"Lugar": bita["place"], "Operador": bita["operador"] })
        return render(request, 'datos.html', {'bitas':bita})


def bitacora(request):
    context = {}
    if request.method == 'GET':
        return render(request,'bitacora.html', {'bita':{}})
    if request.method == 'POST':
        form = BitacoraForm(request.POST or None, request.FILES)
        upload_file = request.FILES['file']
        
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
            fs = FileSystemStorage()
            name = fs.save(upload_file.name, upload_file)
            context['url'] = fs.url(name)

           # handle_uploaded_file(request.FILES['file'])

        myDB = connectDB()
        bitacora = myDB["Bitacora"]
        bitacora.insert_one( { "Fecha": fecha ,"Hora": hour, "Lugar": place, "Operador": operator, "Latitud": latitude, "Longitud": longitude, 
        "Altitud": altitude, "Statype": statype, "Senstype": senstype, "Statnum": statnum, "Sensnum": sensnum, "FlName": flname, "Freq" : freq,
        "Duration": duration, "WindOpts": windopts, "RainOpts":rainopts, "Temp":temp, "RemarksTemp":remarkstemp, "GroundType": groundtyp,
        "RemarksGround": remarksgro, "Observations": observations } )
        return render(request, 'datos.html', context)
        



            

def datos(request):
    return render(request,"datos.html")

def aboutus(request):
    return render(request,"aboutus.html")

def maps(request):
    return render(request,"maps.html")




