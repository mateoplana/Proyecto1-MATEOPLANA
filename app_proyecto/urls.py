from django.urls import path
from .views import *

urlpatterns=[
    path("usuario/", formulariousuario, name="usuarios" ),
    path("moderador/", formulariomoderador, name="moderador"),
    path("usuariofiel/", formulariousuariofiel, name="usuariofiel"),

]