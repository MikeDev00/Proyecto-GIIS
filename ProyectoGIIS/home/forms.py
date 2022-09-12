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
    latitude= forms.FloatField(required=False)
    longitude= forms.FloatField(required=False)
    altitude= forms.FloatField(required=False)
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
    ('Seleccionar...', 'Seleccionar...'),
    ('ETNA ALTUS SERIES', 'ETNA ALTUS SERIES'),
    ('GEOTINY', 'GEOTINY'),
)

VIENTO = (
    ('', 'Seleccionar...'),
    ('1', 'None'),
    ('2', 'Débil (5 m/s)'),
    ('3', 'Medio'),
    ('4', 'Fuerte'),
)

LLUVIA = (
    ('', 'Seleccionar...'),
    ('1', 'None'),
    ('2', 'Débil (5 m/s)'),
    ('3', 'Medio'),
    ('4', 'Fuerte'),
)

TIERRA = (
    ('', 'Seleccionar...'),
    ('1', 'None'),
    ('2', 'Grava'),
    ('3', 'Arena'),
    ('4', 'Roca'),
    ('5', 'Asfalto'),
    ('6', 'Hierba'),
    ('7', 'Cemento'),
    ('8', 'Concreto'),
    ('9', 'Pavimentado'),
)



class PruebaBitaForm(forms.ModelForm):
    place = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Insertar Lugar'}),required=False)
    operator = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Insertar Operador'}),required=False)
    latitude= forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Latitud'}),required=False)
    longitude= forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Longitud'}),required=False)
    altitude= forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Altitud'}),required=False)
    statype =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insertar tipo de estación'}),empty_value=None, required=False)
   
    statnum  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insertar # de estación'}),empty_value=None, required=False)
    sensnum = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insertar # de sensor'}),empty_value=None, required=False)
    flname  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insertar nombre de archivo'}),empty_value=None, required=False)
    freq = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Frecuencia'}),required=False)
    duration  = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Duración'}),required=False)
    
    temp = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Temperatura'}),required=False)
    remarkstemp = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insertar Remarks'}),empty_value=None, required=False)
   
    remarksgro = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insertar remarks'}),empty_value=None, required=False)
   

    senstype = forms.ChoiceField(choices=SENSORES)
    windopts = forms.ChoiceField(choices=VIENTO)
    rainopts = forms.ChoiceField(choices=LLUVIA)
    groundtyp = forms.ChoiceField(choices=TIERRA)
    documento = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


    class Meta:
        model=PruebaBit
        fields = (
        'fecha', 'hour', 'place', 'operator',
        'latitude', 'longitude', 'altitude',
        'statype', 'senstype', 'statnum', 'sensnum',
        'flname', 'freq', 'duration', 'windopts',
        'rainopts', 'temp', 'remarkstemp', 
        'groundtyp', 'remarksgro', 
        'observations', 'is_completed','revisado','nombre', 'autor', 'documento',)
        

        widgets = {
            
            'fecha': DateTimeInput(attrs={'class': 'form-control'}),
            'hour': DateTimeInput2(attrs={'class': 'form-control'}),
   
        }
