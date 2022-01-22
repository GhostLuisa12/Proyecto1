from pipes import Template
from django.shortcuts import render , redirect
from.models import persona
from apps.users.models import persona
from apps.users.forms import usuarioform
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as auth_login




def costumLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Entra aca")
            login(request, user)
            print("sale de aca")
            #return HttpResponseRedirect('listUsers')
            return redirect("index")
        else:
             return redirect('login')
        # Redirect to a success page.
    else:
         return render(request,'login.html')


def listUsers(request):
    listUsuarios= persona.objects.all()
    print('estoy imprimiendo')
    Contexto = {
        'usuarios' : listUsuarios
    }    
    return render(request,"ListaUsuarios.html",Contexto)

def crearUsuario(request):
    if request.method == 'GET':
        form = usuarioform()
    else:
        form = usuarioform(request.POST, request.FILES) 
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listUsers')
    contexto = {
            'form':form
        }

    return render(request,'crearUsuario.html',contexto)

def editarUsuario(request,pk):
    usuario = persona.objects.get(id= pk)
    if request.method == 'GET':
        form = usuarioform(instance=usuario)
    else:
        form = usuarioform(request.POST, request.FILES, instance = usuario) 
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listUsers')
    contexto = {
            'form':form
        }    
    return render(request,'crearUsuario.html',contexto)

class eliminarUsuario(DeleteView):
    model= persona
    template_name= 'eliminarUsuario.html'
    success_url = reverse_lazy('listUsers')