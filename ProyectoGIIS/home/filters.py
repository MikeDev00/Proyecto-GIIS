from dataclasses import fields
from pyexpat import model
import django_filters
from .models import PruebaBit
#from .models import BitacoraInfo
#from .forms import BitacoraForm

import django_filters
 
class UserFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    autor = django_filters.CharFilter(lookup_expr='icontains')
   
    class Meta:
        model = PruebaBit
        fields = ['nombre','autor']

class BitFilter(django_filters.FilterSet):
    operator = django_filters.CharFilter(lookup_expr='icontains')
    place = django_filters.CharFilter(lookup_expr='icontains')
    senstype = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PruebaBit
        fields = ['operator', 'fecha', 'place', 'senstype']