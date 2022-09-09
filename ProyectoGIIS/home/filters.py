import django_filters
from .models import Documentos
#from .models import BitacoraInfo
#from .forms import BitacoraForm

import django_filters
 
class UserFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    autor = django_filters.CharFilter(lookup_expr='icontains')
    #documento = django_filters.__file__(lookup_expr='icontains')
    class Meta:
        model = Documentos
        fields = ['nombre','autor']