from dataclasses import fields
from pyexpat import model
from tkinter import Place
from unicodedata import name
import django_filters
from .models import PruebaBit
#from .models import BitacoraInfo
#from .forms import BitacoraForm

import django_filters
 
class UserFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre')
    autor = django_filters.CharFilter(lookup_expr='icontains', label='Autor')
    place = django_filters.CharFilter(lookup_expr='icontains', label='Lugar')
    class Meta:
        model = PruebaBit
        fields = ['nombre','autor','place']

class BitFilter(django_filters.FilterSet):
    operator = django_filters.CharFilter(lookup_expr='icontains', label='Operador')
    fecha = django_filters.DateFilter(lookup_expr='icontains', label='Fecha')
    place= django_filters.CharFilter(lookup_expr='icontains', label='Lugar')
    senstype = django_filters.CharFilter(lookup_expr='icontains', label='Tipo de Sensor' )
    class Meta:
        model = PruebaBit
        fields = ['operator', 'fecha', 'place', 'senstype']