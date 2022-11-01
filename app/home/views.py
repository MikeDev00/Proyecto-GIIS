from atexit import register
from doctest import testfile
import shutil
from xml.dom.minidom import Element
from django.shortcuts import render, redirect, get_object_or_404
import pymongo
from home.models import PruebaBit, BlogPost, Comment, Registros
import zipfile
import os
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

from django.views.generic import UpdateView

from home.filters import UserFilter, BitFilter

from flask import Flask

from django.http import HttpResponse

from .forms import BlogPostForm, ContatoForm, PruebaBitaForm, SolcitudForm

import numpy as np
import matplotlib.pyplot as plt
#import pyfftw as fftw

# conector con la base de datos MongoDb
def connectDB():
    datosBitacora = MongoClient("mongodb://admin:mongoadmin@database1:27017/?authMechanism=DEFAULT&authSource=admin")
    giisDB = datosBitacora.GIIS
    return giisDB


# Primera vista de plataforma 
def home(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')[:3]
    if posts == "":
        messages.success(request, 'No hay Noticias')
        return render(request, 'home.html')
    else:
        return render(request, "home.html", {'posts':posts})
    

# Filtros  en  la pantalla de descarga
def datos(request):
    user_list = PruebaBit.objects.all()
    user_filter = UserFilter(request.GET, queryset= user_list)
    if user_list == "":

        return render(request, 'user_list.html')
    else:
        return render(request, 'user_list.html', {'filter': user_filter})

    
def filterbit (request):
    bit_filt = PruebaBit.objects.all()
    bita_filter = BitFilter(request.GET, queryset= bit_filt)
    if bit_filt == "":
            return render(request, 'datosfilt.html')
    else:
            return render(request, 'datosfilt.html', {'filter': bita_filter})
       
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
                   
                prueba = PruebaBit(
                        documento= f"{nombre}.zip",
                        fecha = request.POST.get('fecha') ,
                        hour = request.POST.get('hour'),
                        place =request.POST.get('place'),
                        operator = request.user,
                        latitude = request.POST.get('latitude'), 
                        longitude = request.POST.get('longitude'), 
                        altitud = request.POST.get('altitude'),
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
                        revisado = request.POST.get('revisado'),
                        nombre = request.POST.get('nombre'),
                        autor = request.POST.get('autor'), 
                        medtype = request.POST.get('medtype'),
                        medición = request.POST.get('medición'),
                        unidad = request.POST.get('unidad'),
                        clima = request.POST.get('clima'),
                        Estruc = request.POST.get('Estruc'),
                        Traf = request.POST.get('Traf'),
                        author = User.objects.get(pk=request.user.id)                        
                        )
                        

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
    return render(request, 'pruebabit.html',  { 'pruebaform': pruebaform })



# pagina sobre nosotros
def aboutus(request):
    return render(request,"aboutus.html")


# pagina del mapa 
def maps(request):
    return render(request,"maps.html")


def Registro(request):
    if request.method=="POST":   
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        centro = request.POST['centro']
        type = request.POST['type']
       
        registro = Registros(first_name = first_name, last_name = last_name, email = email, centro = centro, type = type)
        registro.save()


        return render(request, 'login.html')   
    return render(request, "registro.html")


def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "El Nombre de Usuario o Contraseña son inválidos.")
            return redirect('login')
    else:   
        return render(request, "login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')


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


def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    if posts == "":
        messages.success(request, 'No hay Noticias')
        return render(request, "blog.html")
    else:
        return render(request, "blog.html", {'posts':posts})

    

def Delete_Blog_Post(request, slug):
    posts = BlogPost.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts':posts})






@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "add_blogs.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})


class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'edit_blog_post.html'
    fields = ['title', 'slug','prueba', 'image']
    


def blogs_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        prueba = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content,prueba=prueba, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments})




def error_404(request, exception):
    return(render, '404.html',{})



#Acciones de solicitudes 

def Solicitudes(request):
    bit_filt = Registros.objects.all()
    bita_filter = BitFilter(request.GET, queryset= bit_filt)
    return render(request, 'solicitudes.html',{'filter': bita_filter})



def editsol(request, id):
    bit = get_object_or_404(Registros, id = id)
    data  = {'pruebaform':SolcitudForm(instance=bit) }
    if request.method =='POST':
        pruebaform = SolcitudForm(request.POST, instance=bit)
       
        if pruebaform.is_valid():
        
            pruebaform.save()
            return redirect('Solicitudes')
    else : 
            pruebaform=SolcitudForm()
    return render(request, 'editsol.html',data)

def contato(request):
    form = ContatoForm(request.POST or None) 
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail() 
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm() 
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {'form': form}
    return render(request, 'contato.html', context)