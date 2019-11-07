from django import forms
from django.contrig.admin import widgets
from .models import Animal, Encargado


class HorarioCuidadoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = HorarioCuidado
        fields = ('nombre', 'anio', 'actores')

    def __init__ (self, *args, **kwargs):
        super(HorarioCuidadoForm, self).__init__(*args, **kwargs)
        self.fields["encargado"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["encargado"].help_text = "Ingrese Encargado del Horario"
        self.fields["fecha_cuidado"].queryset = Encargado.objects.all()
        self.fields["animal"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["animal"].help_text = "Ingrese El nombre del animal a cuidar"
        self.fields["fecha_cuidado"].queryset = Animal.objects.all()

class AnimalForm(object):
    class Meta:
        model = Animal
        fields = ('nombre','edad','raza','cantidad',)

class EncargadoForm(object):
    class Meta:
        model = Animal
        fields = ('nombre','apellido','fecha_nac',)
