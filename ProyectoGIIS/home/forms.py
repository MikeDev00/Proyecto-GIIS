from ast import operator
from dataclasses import fields
from email.policy import default

from pyexpat import model
from tkinter import Place
from django import forms

from .models import PruebaBit


class BitacoraForm(forms.ModelForm):
    fecha= forms.CharField(empty_value=None, required=False)
    hour= forms.CharField(empty_value=None, required=False)
    place= forms.CharField(max_length=100, empty_value=None, required=True)
    operator= forms.CharField(max_length=100, empty_value=None, required=False)
    latitude= forms.FloatField(required=True)
    longitude= forms.FloatField(required=True)
    altitude= forms.FloatField(required=True)
    statype =  forms.CharField(empty_value=None, required=False)
    senstype = forms.CharField(empty_value=None, required=False)
    statnum  = forms.CharField(empty_value=None, required=False)
    sensnum = forms.CharField(empty_value=None, required=False)
    flname  = forms.CharField(empty_value=None, required=False)
    freq = forms.FloatField(required=False)
    duration  = forms.FloatField(required=False)
    windopts  = forms.CharField(empty_value=None, required=False)
    rainopts = forms.CharField(empty_value=None, required=False)
    temp = forms.FloatField(required=False)
    remarkstemp = forms.CharField(empty_value=None, required=False)
    groundtyp = forms.CharField(empty_value=None, required=False)
    remarksgro = forms.CharField(empty_value=None, required=False)
    observations = forms.CharField(empty_value=None, required=False)
   
  
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
    ('Cemento', 'Cemento'),
    ('Concreto', 'Concreto'),
    ('Pavimentado', 'Pavimentado'),
)



class PruebaBitaForm(forms.ModelForm):
    place = forms.CharField( label='Lugar',widget=forms.TextInput(attrs={'placeholder': 'Insertar Lugar'}),required=False)
    operator = forms.CharField( label='Operador',widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)
    latitude= forms.FloatField(label='Latitud', widget=forms.TextInput(attrs={'placeholder': 'Insertar Latitud'}),required=True)
    longitude= forms.FloatField(label='Longitud', widget=forms.TextInput(attrs={'placeholder': 'Insertar Longitud'}),required=True)
    altitude= forms.FloatField(label='Altitud',widget=forms.TextInput(attrs={'placeholder': 'Insertar Altitud'}),required=True)
    statype =  forms.CharField(label='Tipo de Estación',widget=forms.TextInput(attrs={'placeholder': 'Insertar tipo de estación'}),empty_value=None, required=False)
    statnum  = forms.CharField(label='Número de Estación',widget=forms.TextInput(attrs={'placeholder': 'Insertar # de estación'}),empty_value=None, required=False)
    sensnum = forms.CharField(label='Número de Sensor',widget=forms.TextInput(attrs={'placeholder': 'Insertar # de sensor'}),empty_value=None, required=False)
    freq = forms.FloatField(label='Frecuencia Inicial (Hz)',widget=forms.TextInput(attrs={'placeholder': 'Insertar Frecuencia'}),required=True)
    freq2 = forms.FloatField(label='Frecuencia Final (Hz)',widget=forms.TextInput(attrs={'placeholder': 'Insertar Frecuencia'}),required=True)
    duration  = forms.FloatField(label='Duración',widget=forms.TextInput(attrs={'placeholder': 'Insertar Duración'}),required=True)
    temp = forms.FloatField(label='Temperatura',widget=forms.TextInput(attrs={'placeholder': 'Insertar Temperatura'}),required=True)
    remarkstemp = forms.CharField(label='Observaciones de Temperatura',widget=forms.TextInput(attrs={'placeholder': 'Insertar Remarks'}),empty_value=None, required=False)
   
    remarksgro = forms.CharField(label='Observaciones de Tierra',widget=forms.TextInput(attrs={'placeholder': 'Insertar remarks'}),empty_value=None, required=False)
   
    nombre = forms.CharField(label='Nombre del Archivo', widget=forms.TextInput(attrs={'placeholder': 'Inserte el nombre del archivo'}),empty_value=None, required=True)
    senstype = forms.ChoiceField(label='Tipo de Sensor', choices=SENSORES)
    windopts = forms.ChoiceField(label='Condiciones de Viento',choices=VIENTO)
    rainopts = forms.ChoiceField(label='Condiciones de Lluvia',choices=LLUVIA)
    groundtyp = forms.ChoiceField(label='Tipo de Suelo',choices=TIERRA)
    documento = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


    class Meta:
        model=PruebaBit
        fields = (
        'fecha', 'hour', 'place', 'operator',
        'latitude', 'longitude', 'altitude',
        'statype', 'senstype', 'statnum', 'sensnum',
        'freq','freq2', 'duration', 'windopts',
        'rainopts', 'temp', 'remarkstemp', 
        'groundtyp', 'remarksgro', 
        'observations', 'is_completed','revisado','nombre', 'autor', 'documento',)
        

        widgets = {
            
            'fecha': DateTimeInput(attrs={'class': 'form-control'}),
            'hour': DateTimeInput2(attrs={'class': 'form-control'}),
   
        }
