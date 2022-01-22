
from pipes import Template
from django.shortcuts import render , redirect
from.models import persona
from apps.turns.models import turnos
from apps.turns.forms import turnosform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    listTurnos= turnos.objects.all()
    for app in listTurnos:
        print('lista de turnos:: ')
    print('estoy imprimiendo')
    Contexto = {
        'turnos' : listTurnos
    }    
    return render(request,"index.html",Contexto)

def crearTurno(request):
    if request.method == 'GET':
        form = turnosform()
    else:
        form = turnosform(request.POST) 
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    contexto = {
            'form':form
        }

    return render(request,'crearTurnos.html',contexto)

def editarTurno(request,pk):
    turno =turnos.objects.get(id= pk)
    if request.method == 'GET':
        form = turnosform(instance=turno)
    else:
        form = turnosform(request.POST, instance = turno) 
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    contexto = {
            'form':form
        }    
    return render(request,'crearTurnos.html',contexto)

#def eliminarTurno(request,pk):   
 #   turno = turnos.objects.get(id = pk)
  #  turno.delete()
   # return redirect('index')

class eliminarTurno(DeleteView):
    model= turnos
    template_name= 'verificacion.html'
    success_url = reverse_lazy('index')

def cambiarEstado(request,pk):
    turno = turnos.objects.get(id=pk)
    print("turno:::",turno.state.id)
    if turno.state.id == 1:
        print("entra aca")
        turno.state_id = 2
        turno.save()
        print("turno 2:", turno.state_id)
    elif turno.state.id == 2:
        turno.state_id = 3
        turno.save()
    elif turno.state.id == 3:
        turno.state_id = 1
        turno.save()
    return redirect('index')
    


def listTurnsPendientes(request):
    listTurnos= turnos.objects.filter(state_id=1).order_by('created_at')[:5]
    Contexto = {
        'turnos' : listTurnos
    }    
    return render(request,"index.html",Contexto)


