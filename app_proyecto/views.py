from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def formulariousuario(request):

    if request.method == "POST":


        formu=userformulario(request.POST)

        print(formu)

        if formu.is_valid:

            info=formu.cleaned_data

            user = usuarioclass (nombre=info['nombre'], usuario=info['nombre de  usuario'], antiguedad=info['antiguedad usuario'] )

            user.save()
        
            return render(request,"inicio.html")
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
        
            return render(request,"inicio.html")
    else:
        formu2=modformulario()

        return render(request,"moderadores.html", {"formu2":formu2} )


def formulariousuariofiel(request):

    if request.method == "POST":


        formu2=usuarioflformulario(request.POST)

        print(formu2)

        if formu2.is_valid:

            info1=formu2.cleaned_data

            userf = usuarioclass (nombre=info1['nombre'], usuario=info1['nombre de  usuario'], antiguedad=info1['antiguedad usuario'] )

            userf.save()
        
            return render(request,"inicio.html")
    else:
        formu2=usuarioflformulario()

        return render(request,"usuariosfieles.html", {"formu2":formu2} )