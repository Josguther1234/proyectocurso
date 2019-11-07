from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^animal/nueva/$', views.animal_nuevo, name='animal_nuevo'),
    ]
