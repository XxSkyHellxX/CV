from django.urls import path,include
from .views import *

urlpatterns=[
    path('',index,name="index"),
    path('perfil/',perfil,name='perfil'),
    path('misionPerfil/',quienesSomos,name='quienesSomos'),
    path('Galeria/',Galeria,name='galeria'),
    path('registro/',registro,name='registro'),
    path('iniciarSesion/',iniciarSesion,name='iniciarSesion'),
    path('registroProducto/',registroProductos,name='registroProducto'),
    path('eliminar/<int:id>/', Eliminar, name="eliminar"),
    path('eliminarUsuario/<id>',EliminarUsuario,name='eliminarUsuario'),
    path('salir',salir,name='salir'),
    path('modificar/<id>',Modificar,name='modificar'),
    path('feriados/',feriados,name='feriados'),
    path('EliminarCarro/<id>',EliminarCarro,name='eliminar'),
    path('Boleta',Boleta,name='boleta'),
    path('modificarStock',modificarStock,name='modificarStock')
]