from django.contrib import admin
from animal.models import Animal, Encargado, AnimalAdmin, EncargadoAdmin

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Encargado, EncargadoAdmin)
