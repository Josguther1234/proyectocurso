from django.db import models
from django.contrib import admin

class Animal(models.Model):
    nombre  =   models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Encargado(models.Model):
    nombre    = models.CharField(max_length=60)
    apellido  = models.CharField(max_length=60)
    fecha_nac = models.DateField()
    actores   = models.ManyToManyField(Actor, through='Actuacion')

    def __str__(self):
        return self.nombre

class HorarioCuidado(admin.TabularInline):
    model = Actuacion
    extra = 1


class AnimalAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)


class EncargadoAdmin (admin.ModelAdmin):

    inlines = (ActuacionInLine,)
