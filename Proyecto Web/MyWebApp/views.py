from django.shortcuts import render,redirect
from .models import *
import random
from .forms import usuarioForm,productoForm,carritoForm
datosUser={}
# Create your views here.

def feriados(request):
    return render(request,'feriados.html',datosUser)


def registroProductos(request):
    if request.method == "POST":
        producto = productoForm(request.POST,request.FILES)
        if producto.is_valid():
            producto.save()
            return redirect('index')
    else:
        producto = productoForm()
    return render(request,'registroProducto.html',{'producto':producto, **datosUser})

def perfil(request):
    return render(request,'perfil.html',datosUser)

def index(request):
    productos = Productos.objects.all()
    datosUser['galeria']=productos 

    return render(request,'index.html',datosUser)

def quienesSomos(request):
    return render(request,'misionVision.html',datosUser)

def Galeria(request):
    #Carrito
    if request.method=="POST":
        carrito=carritoForm(request.POST,request.FILES)
        if carrito.is_valid():
            carrito.save()
            return redirect('perfil')
        else:
            return redirect('index')
    else:
        carrito = carritoForm()    
    return render(request,'Galeria.html',{'carrito':carrito,**datosUser})

def registro(request):
    if request.method == "POST":
        usuarioform = usuarioForm(request.POST,request.FILES)
        if usuarioform.is_valid():
            usuarioform.save()
            return redirect('iniciarSesion')
    else:
        usuarioform = usuarioForm()
    return render(request, 'registro.html', {'usuarioform': usuarioform})

def iniciarSesion(request):    
    if request.method == "POST":
        usuario= request.POST['username']
        contrasena = request.POST['password']
        try:
            user=Usuario.objects.get(nombre_usuario=usuario,contrasena=contrasena)            
            #Productos Usuarios
            datosUser['idUsuario']=user.id_usuario
            datosUser['nombreReal']=user.nombre_real
            datosUser['apellidos']=user.apellidos
            datosUser['nombreUser']=user.nombre_usuario
            datosUser['rut']=user.rut
            datosUser['comuna']=user.comuna
            datosUser['celular']=user.celular
            datosUser['direccion']=user.direccion
            datosUser['correo']=user.correo
            datosUser['imagen']=user.imagen
            productos=Productos.objects.filter(usuarioProp=datosUser['idUsuario'])
            datosUser['productos']=productos
            datosUser['usuarios']=Usuario.objects.all()
            datosUser['carro']=Carrito_Valido.objects.filter(usuario=datosUser['idUsuario'])

        
            return redirect('perfil')
        except Usuario.DoesNotExist:
            try:
                admin= UsuarioADM.objects.get(nombre_usuario_adm=usuario,contrasena_adm=contrasena)
                datosUser['productosadm']=Productos.objects.all()
                datosUser['id_usuario_adm']=admin.id_usuario_adm
                datosUser['nombreADMIN']=admin.nombre_usuario_adm                    
                datosUser['usuarios']=Usuario.objects.all()
                datosUser['carro']=Carrito.objects.all()
                return redirect('perfil')
            except:
                error_message = "Credenciales no validas"    
                return render(request,'login.html',{'error_message':error_message})            
    else:            
        return render(request, 'login.html')
    
def Eliminar(request,id):
    productoEliminado=Productos.objects.get(id_producto=id) 
    productoEliminado.delete()
    return redirect('index')

def EliminarUsuario(request,id):
    usuarioEliminado = Usuario.objects.get(id_usuario=id)
    usuarioEliminado.delete()
    return redirect('index')

def EliminarCarro(request,id):
    carroEliminado = Carrito_Valido.objects.get(id_producto_carrito=id)
    carroEliminado.delete()
    return redirect('perfil')

def Modificar(request,id):
    productoModificado=Productos.objects.get(id_producto=id)

    if request.method=="POST":
        formulario = productoForm(data=request.POST,files=request.FILES,instance=productoModificado)
        productoModificado.usuarioProp= None
        productoModificado.titulo_producto = ""
        productoModificado.descripcion=""
        productoModificado.precio=0
        productoModificado.stock=0
        productoModificado.categoria=None
        productoModificado.imagen=None
        if formulario.is_valid():   
            formulario.save()
            productoModificado.save()
            return redirect('index')
        else:
            return redirect('perfil')
    else:
        formulario=productoForm(instance=productoModificado)    
    return render(request,'modificarProducto.html',{'form':productoForm(instance=productoModificado),**datosUser})

def salir(request):    
    datosUser.clear()
    return redirect('iniciarSesion')

def Boleta(request): 
    return render(request,'Boleta.html',datosUser)

def modificarStock(request):

    carro = datosUser['carro']

    for i in carro:
        productoModificado = Productos.objects.get(id_producto=i.producto.id_producto)

        productoModificado.stock-=i.cantidad
        
    productoModificado.save()
    
    Carrito_Valido.objects.all().delete()

    return redirect('index')    