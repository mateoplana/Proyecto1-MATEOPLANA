from django.urls import path
from .views import *

urlpatterns=[
    path("usuario/", formulariousuario, name="usuarios" ),
    path("moderador/", formulariomoderador, name="moderador"),
    path("usuariofiel/", formulariousuariofiel, name="usuariofiel"),
    path("busquedausuario/", busquedausuario, name="busquedausuario"),
    path("buscarusuario", buscarusuario, name="buscarusuario"),
    path("busquedausuariofiel/", busquedausuariofiel, name="busquedausuariofiel"),
    path("buscarusuariofiel", buscarusuariofiel, name="buscarusuariofiel"),
    path("busquedamoderador/", busquedamoderador, name="busquedamoderador"),
    path("buscarmoderador", buscarmoderador, name="buscarmoderador"),


]