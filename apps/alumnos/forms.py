from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control'                    
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control'                    
                }
            ),
            'cedula': forms.NumberInput(
                attrs = {
                    'class': 'form-control'                    
                }
            ),
            'genero': forms.Select(
                attrs = {
                    'class': 'form-control'                    
                }
            ),
            'foto': forms.FileInput(
                attrs = {
                    'class': 'form-control-file'                    
                }
            ),





        }


