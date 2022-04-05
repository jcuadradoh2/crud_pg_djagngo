from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import index, AlumnoCreate, AlumnoUpdate, AlumnoDelete

urlpatterns = [
    path('', index, name='index'),
    path('alumno/create', AlumnoCreate, name='alumno_create'),
    path('alumno/update/<pk>', AlumnoUpdate, name='alumno_update'),
    path('alumno/delete/<pk>', AlumnoDelete, name='alumno_delete'),
]
