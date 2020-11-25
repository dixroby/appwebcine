
from django import forms
from django.forms import ModelForm
from .models import Pelicula
import datetime
class PeliculaForm(ModelForm):
    nombre = forms.CharField(min_length = 2, max_length = 300)
    duracion = forms.IntegerField(min_value=5,max_value=10000)
    class Meta:
        model = Pelicula
        fields = ['nombre','duracion','anio','genero','fecha_streno','sipnopsis','imagen']

        widgets = {
            'fecha_streno' : forms.SelectDateWidget(years = range(1990,2021 ))
        }
    def clean_fecha_streno(self):

        fecha = self.cleaned_data['fecha_streno']

        if fecha > datetime.date.today() :
            raise forms.ValidationError("La fecha no puede ser mayor al dia de hoy") #excepcion

        return fecha 
