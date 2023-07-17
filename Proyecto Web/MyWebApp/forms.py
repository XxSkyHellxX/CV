from django import forms
from .models import Usuario,Productos,Carrito_Valido


class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_real','apellidos','nombre_usuario','contrasena','re_contrasena','rut','comuna','celular','direccion','correo','imagen']
        labels = {
            'nombre_real':'Nombre',
            'apellidos':'Apellidos',
            'nombre_usuario':'Usuario',
            'contrasena':'Contraseña',
            're_contrasena':'Reingresa la contraseña',
            'rut':'Rut',
            'comuna':'Comuna',
            'celular':'Celular',
            'direccion':'Direccion',
            'correo':'Correo',
            'imagen':'Imagen De Perfil'
        }
        widgets={
            'nombre_real':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su nombre',
                    'id':'nom',
                    'name':'nom',
                    'class':'form-control mb-2 input',
                    'style':'border: 1px solid rgb(229, 69, 11)',                    
                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus apellidos',
                    'id':'apellidos',
                    'class':'form-control mb-2',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'nombre_usuario':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre de usuario',
                    'id':'usuario',
                    'name':'usuario',
                    'class':'form-control mb-2',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'contrasena':forms.PasswordInput(
                attrs={
                    'placeholder':'Ingrese una contraseña',
                    'id':'pass',
                    'class':'form-control mb-2',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            're_contrasena':forms.PasswordInput(
                attrs={
                    'placeholder':'Reingrese su contraseña',
                    'id':'pass2',
                    'class':'form-control mb-2',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'rut':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su rut, ejemplo: 20.780.876-8',
                    'id':'rut',
                    'class':'form-control mb-2',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'comuna':forms.Select(
                attrs={
                    'id':'comuna',
                    'class':'mb-2 rounded p-1 formuOpt l',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'celular':forms.NumberInput(
                attrs={
                    'placeholder':'ingrese su numero de celular',
                    'id':'celular',
                    'class':'form-control mb-2',
                    'style':'border: 1px solid rgb(229, 69, 11)'             
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su direccion',
                    'id':'direccion',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'correo':forms.EmailInput(
                attrs={
                    'placeholder':'Ingrese su email',
                    'id':'correo',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id':'imagen',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',                    
                }
            )
        }

class productoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields= ['usuarioProp','titulo_producto','descripcion','categoria','stock','precio','imagen']
        labels={
            'usuarioProp':'PROPIETARIO',
            'titulo_producto':'Titulo',
            'descripcion':'Descripcion',
            'precio':'Precio',
            'categoria':'Categoria',
            'stock':'Stock',
            'imagen':'Imagen'
        }
        widgets={
            'usuarioProp':forms.Select(
                attrs={
                    'id':'usuarioProp',
                    'name':'usuarioProp',
                    'class':'form-control mb-3 formuOpt ',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'titulo_producto':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese un titulo para su producto',
                    'id':'titulo',
                    'name':'titulo',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'placeholder':'Ingrese una descripcion para su producto (300 palabras max)',
                    'id':'descripcion',
                    'name':'descripcion',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',
                    'rows':4,
                    'cols':40
                }
            ),
            'categoria':forms.Select(
                attrs={                    
                    'id':'categoria',
                    'name':'categoria',
                    'class':'form-control mb-3 formuOpt',
                    'style':'border: 1px solid rgb(229, 69, 11)',                    
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'id':'precio',
                    'name':'precio',
                    'placeholder':'Ingrese un precio (maximo 9 digitos)',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',                    
                }
            ),
            'stock':forms.NumberInput(
                attrs={
                    'id':'stock',
                    'name':'stock',
                    'placeholder':'Ingrese cuanto stock tiene disponible',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',                          
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id':'imagen',
                    'name':'imagen',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',     
                    'required':False               
                }
            )
        }

class carritoForm(forms.ModelForm):
    class Meta:
        model = Carrito_Valido
        fields= ['usuario','producto','cantidad']
        labels={
            'usuario':'usuario',
            'producto':'producto',
            'cantidad':'Cantidad',
        }
        widgets={
            'usuario':forms.NumberInput(
                attrs={
                    'id':'usuario',
                    'name':'usuario',
                    'class':'form-control mb-3 ',
                    'style':'border: 1px solid rgb(229, 69, 11)',
                }
            ),
            'producto':forms.NumberInput(
                attrs={
                    'id':'producto',
                    'name':'producto',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',
                }
            ),
            'cantidad':forms.NumberInput(
                attrs={
                    'id':'cantidad',
                    'name':'cantidad',
                    'class':'form-control mb-3',
                    'style':'border: 1px solid rgb(229, 69, 11)',
                }
            )
        }

