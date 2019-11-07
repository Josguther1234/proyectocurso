from django.shortcuts import render
from django.contrib import messages
from .forms import AnimalForm
from animal.models import Animal, Encargado

def Horario_Huevo(request):
    if request.method == "POST":
        formulario = HorarioCuidadoForm(request.POST)
        if formulario.is_valid():
            animal = Animal.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for encargado_id in request.POST.getlist('encargado'):
                horario = Actuacion(animal_id=animal_id, encargado_id = encargado.id)
                horario.save()
            messages.add_message(request, messages.SUCCESS, 'Horario Guardado con Exito')
    else:
        formulario = HorarioCuidadoForm()
    return render(request, 'horario/horario_editar.html', {'formulario': formulario})
