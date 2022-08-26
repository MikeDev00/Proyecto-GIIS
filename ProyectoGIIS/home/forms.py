from email.policy import default
from django import forms

class CarForm(forms.Form):
    id= forms.IntegerField()
    name= forms.CharField(max_length=100)
    year= forms.IntegerField()
    price= forms.FloatField()


class BitacoraForm(forms.Form):
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
    file = forms.FileField()
    
