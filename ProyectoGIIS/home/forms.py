from ast import operator
from collections import UserList
from dataclasses import fields
from email.policy import default
from mimetypes import init
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from pyexpat import model
from tkinter import Place
from django import forms

from .models import BlogPost, PruebaBit, Registros


  
class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class DateTimeInput2(forms.DateTimeInput):
    input_type = 'time'
    
SENSORES = (
    ('', 'Seleccionar...'),
    ('ETNA ALTUS SERIES', 'ETNA ALTUS SERIES'),
    ('GEOTINY', 'GEOTINY'),
)

VIENTO = (
    ('', 'Seleccionar...'),
    ('None', 'None'),
    ('Débil (5 m/s)', 'Débil (5 m/s)'),
    ('Medio', 'Medio'),
    ('Fuerte', 'Fuerte'),
)

LLUVIA = (
    ('', 'Seleccionar...'),
    ('None', 'None'),
    ('Débil (5 m/s)', 'Débil (5 m/s)'),
    ('Medio', 'Medio'),
    ('Fuerte', 'Fuerte'),
)

TIERRA = (
    ('', 'Seleccionar...'),
    ('None', 'None'),
    ('Grava', 'Grava'),
    ('Arena', 'Arena'),
    ('Roca', 'Roca'),
    ('Asfalto', 'Asfalto'),
    ('Hierba', 'Hierba'),
    ('Concreto', 'Concreto'),
)


CLIMA = (
    ('', 'Seleccionar...'),
    ('Lluvioso', 'Lluvioso'),
    ('Soleado', 'Soleado'),
    ('Nublado', 'Nublado'),
)


TRAFICO = (
    ('', 'Seleccionar...'),
    ('Denso', 'Denso (Vehículo en Tranque)'),
    ('Moderado', 'Moderado (constante)'),
    ('Bajo', 'Bajo ( Menor de 20 Vehiculos durante la medición)'),
    ('Nulo', 'Nulo'),
)


ESTRUC = (
    ('', 'Seleccionar...'),
    ('Denso', 'Denso (Locales Comerciales)'),
    ('Moderado', 'Moderado (Residencias)'),
    ('Bajo', 'Bajo ( Arboles, Cercas, Etc...)'),
    ('Nulo', 'Nulo'),
)


ESTACION = (
    ('', 'Seleccionar...'),
    ('Móvil', 'Móvil'),
    ('Fijo', 'Fijo'),
)





class PruebaBitaForm(forms.ModelForm):

    place = forms.CharField( label='Lugar',widget=forms.TextInput(attrs={'placeholder': 'Insertar Lugar'}, ),required=False)
    operator = forms.CharField( label='Operador',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False )
    latitude= forms.FloatField(label='Latitud', widget=forms.TextInput(attrs={'placeholder': 'Insertar Latitud'}),required=True)
    longitude= forms.FloatField(label='Longitud', widget=forms.TextInput(attrs={'placeholder': 'Insertar Longitud'}),required=True)
    altitud= forms.DecimalField(label='Altitud',widget=forms.TextInput(attrs={'placeholder': 'Insertar Altitud'}),required=False)
    statnum  = forms.CharField(label='Número de Medición',widget=forms.TextInput(attrs={'placeholder': 'Insertar # de Medición'}),empty_value=None, required=False)
    sensnum = forms.CharField(label='Número de Sensor',widget=forms.TextInput(attrs={'placeholder': 'Insertar # de sensor'}),empty_value=None, required=False)
    freq = forms.FloatField(label='Frecuencia Inicial (Hz)',widget=forms.TextInput(attrs={'placeholder': 'Insertar Frecuencia'}),required=True)
    freq2 = forms.FloatField(label='Frecuencia Final (Hz)',widget=forms.TextInput(attrs={'placeholder': 'Insertar Frecuencia'}),required=True)
    duration  = forms.FloatField(label='Duración (Min)',widget=forms.TextInput(attrs={'placeholder': 'Insertar Duración'}),required=True)
    temp = forms.FloatField(label='Temperatura',widget=forms.TextInput(attrs={'placeholder': 'Insertar Temperatura'}),required=True)
    remarkstemp = forms.CharField(label='Observaciones de Temperatura',widget=forms.TextInput(attrs={'placeholder': 'Insertar Remarks'}),empty_value=None, required=False)
    remarksgro = forms.CharField(label='Observaciones de Tierra',widget=forms.TextInput(attrs={'placeholder': 'Insertar remarks'}),empty_value=None, required=False)
    nombre = forms.CharField(label='Nombre del Archivo', widget=forms.TextInput(attrs={'placeholder': 'Inserte el nombre del archivo'}),empty_value=None, required=True)
    Estruc = forms.ChoiceField(label='Estructuras Cercanas',choices=ESTRUC)
    Traf = forms.ChoiceField(label='Tráfico',choices=TRAFICO)
    clima =  forms.ChoiceField(label='Tipo de Estación',choices=CLIMA)
    statype =  forms.ChoiceField(label='Tipo de Estación',choices=ESTACION)
    senstype = forms.ChoiceField(label='Tipo de Sensor', choices=SENSORES)
    windopts = forms.ChoiceField(label='Condiciones de Viento',choices=VIENTO)
    rainopts = forms.ChoiceField(label='Condiciones de Lluvia',choices=LLUVIA)
    groundtyp = forms.ChoiceField(label='Tipo de Suelo',choices=TIERRA)
    documento = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    medtype = forms.CharField(label='Tipo de Medición', widget=forms.TextInput(attrs={'placeholder': ''}),required=False )
    medición = forms.DecimalField(label='Medición', widget=forms.TextInput(attrs={'placeholder': ''}),required=False)
    unidad = forms.CharField(label='Unidad', widget=forms.TextInput(attrs={'placeholder': ''}),required=False)

    class Meta:
        model=PruebaBit
        fields = (
        'fecha', 'hour', 'place', 'operator',
        'latitude', 'longitude', 'altitud',
        'statype', 'senstype', 'statnum', 'sensnum',
        'freq','freq2', 'duration', 'windopts',
        'rainopts', 'temp','clima', 'remarkstemp', 
        'groundtyp', 'remarksgro', 
        'Estruc','Traf',
        'observations', 'is_completed','revisado','nombre', 'autor',
        'documento', 'medtype', 'medición', 'unidad')
        

        widgets = {
            
            'fecha': DateTimeInput(attrs={'class': 'form-control'}),
            'hour': DateTimeInput2(attrs={'class': 'form-control'}),
   
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'prueba','image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título del Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copie el título sin espacios y con un guión en el medio'}),
            'prueba': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Contenido del Blog'}),
        }


class SolcitudForm(forms.ModelForm):
     first_name = forms.CharField( label='Nombre',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)
     last_name = forms.CharField( label='Apellido',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)
     email = forms.CharField( label='Email',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)
     centro = forms.CharField( label='Sede',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)
     type = forms.CharField( label='Tipo de Usuario',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)

     class Meta:
        model=Registros
        fields = (
            'first_name','last_name',
            'email','centro', 'type',
            'observaciones' , 'revisado'
        )


# modelos do formulario de contato
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # funcao que envia email mail
    def send_mail(self): 
        email = self.cleaned_data['email'] 
  
        subject = 'E-mail enviado django'
        html_message = render_to_string('sendmail.html')
        plain_message = strip_tags(html_message)
        from_email='seu email'
        to= email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
