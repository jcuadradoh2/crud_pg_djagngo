from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

def index(request):
    alumno = Alumno.objects.all()
    context = {
        'alumnos': alumno
    }
    return render(request, 'alumno/index.html', context)

def AlumnoCreate(request):
    
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    context = {
        'form': form
    }

    return render(request, 'alumno/alumno-create.html', context)


def AlumnoUpdate(request, pk):
    alumno = Alumno.objects.get(id=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm(instance=alumno)
    context = {
        'form': form,
        'alumnos': alumno
    }

    return render(request, 'alumno/alumno-create.html', context)



def AlumnoDelete(request, pk):
    alumno = Alumno.objects.get(id=pk)
    alumno.delete()
    return redirect('index')

