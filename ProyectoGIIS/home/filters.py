from dataclasses import fields
from pyexpat import model
import django_filters
from .models import BitacoraInfo


class SnippetFilter(django_filters.FilterSet):
    class Meta:
        model = BitacoraInfo
        fields = ('fecha','place','operator')