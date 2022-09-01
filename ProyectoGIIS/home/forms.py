from dataclasses import fields
from email.policy import default

from pyexpat import model
from django import forms

from .models import Documentos


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


class DocumentoForm(forms.ModelForm):   
    class Meta:
        model= Documentos
        fields = ( 'nombre', 'autor', 'documento')
    
