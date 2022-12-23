from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.

def formulariousuario(request):

    if request.method == "POST":


        formu=userformulario(request.POST)

        print(formu)

        if formu.is_valid:

            info=formu.cleaned_data

            user = usuarioclass (nombre=info['nombre'], usuario=info['usuario'], antiguedad=info['antiguedad'] )

            user.save()
        
            return render(request,"inicio.html", { "mensaje":"Usuario guardado correctamente" })
    else:
        formu=userformulario()

        return render(request,"usuarios.html", {"formu":formu} )
         
def formulariomoderador(request):

    if request.method == "POST":


        formu2=modformulario(request.POST)

        print(formu2)

        if formu2.is_valid:

            info2=formu2.cleaned_data

            mod = moderador(nombre=info2['nombre'], usuario=info2['usuario'], email=info2['email'] )

            mod.save()
        
            return render(request,"inicio.html", { "mensaje":"Moderador guardado correctamente" })
    else:
        formu2=modformulario()

        return render(request,"moderadores.html", {"formu2":formu2} )


def formulariousuariofiel(request):

    if request.method == "POST":


        formu2=usuarioflformulario(request.POST)

        print(formu2)

        if formu2.is_valid:

            info1=formu2.cleaned_data

            userf = usuario_fiel (nombre=info1['nombre'], usuario=info1['usuario'], antiguedad=info1['antiguedad'] )

            userf.save()
        
            return render(request,"inicio.html", { "mensaje":"Usuario fiel guardado correctamente" })
    else:
        formu2=usuarioflformulario()

        return render(request,"usuariosfieles.html", {"formu2":formu2} )


def busquedausuario(request):
    return render(request, "buscarusuario.html")

def buscarusuario(request):
     
        usuario=request.GET["usuario"]
        if usuario!="":
         usuarios=usuarioclass.objects.filter(usuario=usuario)

         return render(request, "resultadosusuario.html", {"usuarios":usuarios})

        else:
            return render(request, "buscarusuario.html", {"mensaje":"Ingresar un usuario valido"})


def busquedausuariofiel(request):
    return render(request, "buscarusuariofiel.html")

def buscarusuariofiel(request):
     
        usuario=request.GET["usuario"]
        if usuario!="":
         usuarios=usuario_fiel.objects.filter(usuario=usuario)

         return render(request, "resultadosusuariofiel.html", {"usuarios":usuarios})

        else:
            return render(request, "buscarusuariofiel.html", {"mensaje":"Ingresar un usuario valido"})


def busquedamoderador(request):
    return render(request, "buscarmoderador.html")

def buscarmoderador(request):
     
        usuario=request.GET["usuario"]
        if usuario!="":
         usuarios=moderador.objects.filter(usuario=usuario)

         return render(request, "resultadosmoderador.html", {"usuarios":usuarios})

        else:
            return render(request, "buscarmoderador.html", {"mensaje":"Ingresar un usuario valido"})