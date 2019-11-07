from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^animal/nueva/$', views.Horario_Huevo, name='Horario_Huevo'),
    ]
