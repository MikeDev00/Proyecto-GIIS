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
from django.forms import formset_factory

from home.filters import UserFilter, BitFilter


from .forms import BitacoraForm, GraficasFrom, PruebaBitaForm

import numpy as np
import matplotlib.pyplot as plt
#import pyfftw as fftw

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
            "clima":bita["clima"],
            "groundtyp":bita["groundtyp"],
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
                        nombre = request.POST.get('nombre'), 
                        autor = request.POST.get('autor'), 
                        clima = request.POST.get('clima'),
                        Estruc = request.POST.get('Estruc'),
                        Traf = request.POST.get('Traf'), )
                        
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
        altitude = request.POST.get('altitude')
        
        if altitude =='':
            altitude: None
            
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
                        autor = request.POST.get('autor'), 
                        clima = request.POST.get('clima'),
                        Estruc = request.POST.get('Estruc'),
                        Traf = request.POST.get('Traf') 
                        )

                        
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




def Graficas(request):
    if request.method =='POST':
        pruebagraf = GraficasFrom(request.POST, request.FILES)
        documentox = request.FILES.getlist('xarch')
        documentoy = request.FILES.getlist('yarch')
        documentoz = request.FILES.getlist('zarch')
        nombre = request.POST.get('nomx')
        if pruebagraf.is_valid():
            pruebagraf.save()
            data_x= documentox
            data_y= documentoy
            data_z= documentoz 

            #Analysis parameters
            sample_frequency=100.
            time_start=30.
            time_end=1230.
            win_time=120.
            frequency_min=1.
            frequency_max=20.

            #Graph format
            line_color='green'
            font={'family':'times new roman'}
            plt.rc('font',**font)

            #Plot definition
            def plot(axis_y,xi,dx,xmin,xmax,title,xlabel,ylabel,line_color):
                axis_x=np.arange(xi,xi+dx*len(axis_y),dx)
                plt.plot(axis_x,axis_y,line_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.xlim([xmin,xmax])
                plt.grid(True)
                plt.savefig(title+".png")
                plt.show()

            #Setting windows
            files=[data_x,data_y,data_z]
            data=[]
            dt=1/sample_frequency
            i_start=int(time_start*sample_frequency)
            i_end=int(time_end*sample_frequency)
            win_size=int(win_time*sample_frequency)
            win_number=int((i_end-i_start)/win_size)

            #Read files 
            for file in files:
                axis_y=np.genfromtxt(file,delimiter='',dtype=None)
                data.append(np.array(axis_y[i_start:i_end]))
                plot(data[len(data)-1],time_start,dt,time_start,time_end,file,'Time, t (s)','Data',line_color)

            #Print setting parameters
            print('Data =',axis_y.size,' ','Data size =',axis_y[i_start:i_end].size)
            print('Window size =',win_time,'s',' ','Window data size =',win_size,' ','Windows =',win_number)
            print('Time start =',time_start,'s ','Time end =',time_end,'s')
            print('Data start =',i_start,' ','Data end =',i_end)

            #Setting Fast Fourier Transform
            d_x=[i*win_size for i in range(win_number)]
            spectral_ratios=[]
            output=np.empty(int(win_size/2+1),dtype='complex128')
            input_array=np.empty(int(win_size),dtype='float64')
            #fft=fftw.FFTW(input_array,output)

            #Smooth parameters
            index_zoom=1000000
            bandwidth=40
            lower_lim=10**(-np.pi/bandwidth)
            upper_lim=1/lower_lim

            #Setting ranges
            HVy=[]
            HVy_min=int(frequency_min*win_time)
            HVy_max=int(frequency_max*win_time)

            #Setting smooth
            HVy_smooth=np.ones([3,HVy_max])
            weight=np.ones(int(index_zoom*upper_lim+1))
            f_fc_list=np.arange(lower_lim,upper_lim,1/index_zoom)
            f_fc_list=np.delete(f_fc_list,int((1-lower_lim)*index_zoom))

            #Setting Konno & Ohmachi
            for f_fc in f_fc_list:
                argument=bandwidth*np.log10(f_fc)
                index=round(f_fc*index_zoom)
                weight[index]=np.power(np.sin(argument)/(argument),4)

            #Fast Fourier Transform and Konno & Ohmachi smoothing
            frequency_sum=0    
            for a in range(win_number):
                for b in range(3):           
                    fast_fourier=abs(input_array=data[b][d_x[a]:d_x[a]+win_size])
                    for c in range(HVy_min,HVy_max): 
                        sum_weight=0.
                        sum_amp=0.
                        for d in range(int(lower_lim*c),int(upper_lim*c)):
                            f_fc=d/c
                            index=round(f_fc*index_zoom)
                            weight_temp=weight[index] 
                            sum_amp+=fast_fourier[d]*weight_temp
                            sum_weight+=weight_temp
                        HVy_smooth[b][c]=sum_amp/sum_weight
                spectral_ratios.append(np.sqrt(HVy_smooth[0]*HVy_smooth[1])/HVy_smooth[2])
                frequency_sum+=np.argmax(spectral_ratios[a])/win_time

            #Smoothed data
            for i in range(len(spectral_ratios[0])):
                spectral_average=sum(spectral_ratio[i] for spectral_ratio in spectral_ratios)/win_number
                HVy.append(spectral_average)

            #Print frequency and smoothed graph
            print('Average window frequency =',round(frequency_sum/win_number,3),'Hz')
            print('Maximum frequency from graph =',np.argmax(HVy)/win_time,'Hz')
            plot(HVy,0, 1/win_time,frequency_min,frequency_max,'H_V Spectral Ratio','Frequency, f (Hz)','Amplitude',line_color)

            return redirect('graficas')
    else:
        pruebagraf=GraficasFrom()
    return render(request, 'graficas.html', {'pruebagraf':pruebagraf})