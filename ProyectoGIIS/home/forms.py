from django import forms

class CarForm(forms.Form):
    id= forms.IntegerField()
    name= forms.CharField(max_length=100)
    year= forms.IntegerField()
    price= forms.FloatField()


class BitacoraForm(forms.Form):
    fecha= forms.CharField()
    hour= forms.CharField()
    place= forms.CharField(max_length=100)
    operator= forms.CharField(max_length=100)
    latitude= forms.FloatField()
    longitude= forms.FloatField()
    altitude= forms.FloatField()
    statype =  forms.CharField()
    senstype = forms.CharField()
    statnum  = forms.CharField()
    sensnum = forms.CharField()
    flname  = forms.CharField()
    freq = forms.FloatField()
    duration  = forms.FloatField()
    windopts  = forms.CharField()
    rainopts = forms.CharField()
    temp = forms.FloatField()
    remarkstemp = forms.CharField()
    groundtyp = forms.CharField()
    remarksgro = forms.CharField()
    observations = forms.CharField()
    input2 = forms.FileField()



