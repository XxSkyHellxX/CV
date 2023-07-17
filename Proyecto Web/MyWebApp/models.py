from django.db import models
import os
from django.conf import settings
import random
from django.core.files.storage import default_storage
import datetime

#variables
subtotal= 0

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True,verbose_name="ID DE COMUNA")
    nombre_comuna = models.CharField(max_length=50,verbose_name="NOMBRE DE LA COMUNA",null=False)

    def __str__(self):
        return (self.nombre_comuna)
    

class CategoriaProducto(models.Model):
    id_categoria = models.AutoField(primary_key=True,verbose_name="ID CATEGORIA")
    nombre_categoria = models.CharField(max_length=20,verbose_name="NOMBRE CATEGORIA",null=False)

    def __str__(self):
        return str (self.nombre_categoria)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,verbose_name="ID DEL USUARIO")
    nombre_real = models.CharField(max_length=32,verbose_name="NOMBRE REAL DEL USUARIO",null=False)
    apellidos = models.CharField(max_length=60,verbose_name="APELLIDOS DEL USUARIO",null=False)
    nombre_usuario= models.CharField(max_length=20, verbose_name="NOMBRE DE USUARIO",null=False)
    contrasena = models.CharField(max_length=10 , verbose_name="CONTRASEÑA DEL USUARIO",null=False)
    re_contrasena = models.CharField(max_length=10 , verbose_name="CONTRASEÑA DEL USUARIO",null=False)
    rut= models.CharField(max_length=12,verbose_name="RUT DEL USUARIO",null=False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    celular = models.IntegerField(verbose_name="NUMERO DE CONTACTO",null=False)
    direccion = models.CharField(max_length=60,verbose_name="DOMICILIO DEL USUARIO",null=False)
    correo = models.EmailField(verbose_name="CORREO",null=False)
    imagen = models.ImageField(upload_to="imagenes",null=True,verbose_name="IMAGEN",blank=True)
    def __str__(self):
        return str(self.id_usuario)+" "+self.rut+" "+self.nombre_real+" "+self.apellidos+" "+self.nombre_usuario
    
class UsuarioADM(models.Model):
    id_usuario_adm = models.AutoField(primary_key=True,verbose_name="ID DEL USUARIO ADMINISTRADOR")
    nombre_usuario_adm= models.CharField(max_length=20, verbose_name="NOMBRE DE USUARIO ADMINISTRADOR",null=False)
    contrasena_adm = models.CharField(max_length=10 , verbose_name="CONTRASEÑA DEL USUARIO ADMINISTRADOR",null=False)
    re_contrasena_adm = models.CharField(max_length=10 , verbose_name="CONTRASEÑA DEL USUARIO ADMINISTRADOR",null=False)

    def __str__(self):
        return self.nombre_usuario_adm+" "+self.contrasena_adm

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True,verbose_name="ID DEL PRODUCTO")    
    usuarioProp = models.ForeignKey(UsuarioADM,on_delete=models.CASCADE,null=True,)
    titulo_producto = models.CharField(max_length=60,verbose_name="NOMBRE DEL PRODUCTO",null=False)
    descripcion = models.CharField(max_length=300,verbose_name="DESCRIPCION DEL PRODUCTO",null=False)
    precio = models.CharField(max_length=9,verbose_name="PRECIO",default="0")
    categoria = models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE,null=True)
    stock = models.IntegerField(verbose_name="STOCK",default=0)
    imagen = models.ImageField(upload_to="imagenes",null=True,verbose_name="IMAGEN",blank=True)

    def __str__(self):
        return str(self.id_producto) + " " + str(self.usuarioProp) + " " + self.titulo_producto + " " + self.descripcion + " " + self.precio + " " + str(self.categoria) + " " + str(self.stock) + " " + str(self.imagen)
    

class Carrito(models.Model):  
    id_producto_carrito = models.AutoField(primary_key=True,verbose_name="CARRITO ID")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, verbose_name="USUARIO")
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, verbose_name="PRODUCTO")
    cantidad = models.IntegerField(verbose_name="STOCK SOLICITADO",default=0,null=True)  

    def pago(self):
        subtotal = int(self.producto.precio)*int(self.cantidad)
        return subtotal
    
    def __str__(self):
        return str(self.id_producto_carrito)+" "+str(self.usuario)+" "+str(self.producto)+" "+str(self.cantidad)

class Carrito_Valido(models.Model):  
    id_producto_carrito = models.AutoField(primary_key=True,verbose_name="CARRITO ID")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, verbose_name="USUARIO")
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True, verbose_name="PRODUCTO")
    cantidad = models.IntegerField(verbose_name="STOCK SOLICITADO",default=0,null=True)  

    def pago(self):
        subtotal = int(self.producto.precio)*int(self.cantidad)
        return subtotal
    
    def __str__(self):
        return str(self.id_producto_carrito)+" "+str(self.usuario)+" "+str(self.producto)+" "+str(self.cantidad)