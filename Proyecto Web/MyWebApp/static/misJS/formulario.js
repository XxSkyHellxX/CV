$(document).ready(function () {
    $("#miForm").validate({
        rules: {
            nom:{
                required: true
            },
            apellidos: {
                required: true
            },
            usuario:{
                required:true
            },
            pass:{
                required:true,
                minlength:5,
                maxlength:10
            },
            pass2:{
                required:true,
                equalto:'#pass'
            },
            rut:{
                required:true,
                minlength:12
            },
            comuna:{
                required:true
            },
            celular:{
                required:true,
                minlength:9
            },
            direccion:{
                required:true
            },
            correo:{
                required:true
            }
        },
        messages: {
            nom:{
                required: 'Nombre Obligatorio'
            },
            apellidos:{
                required: 'Se necesitan sus dos apellidos'
            },
            usuario:{
                required: 'Ingrese un nombre de usuario'
            },
            pass:{
                required:'Debe ingresar una contraseña',
                minlength: 'Debe contener un minimo de 5 caracteres',
                maxlength: 'Limite de 10 caracteres'
            },
            pass2:{
                required:'Reingresa tu contraseña creada anteriormente',
                equalto: 'La contraseña es diferente a la anterior'
            },
            rut:{
                required:'Se necesita su RUT (Rol Unico Tributario)',
                minlength: 'Su rut esta incompleto, por favor revise'
            },
            comuna:{
                required: 'Se necesita la comuna donde reside actualmente'
            },
            celular:{
                required: 'Se necesita su numero de contacto',
                minlength: 'Numero de celular no valido, anteponga un 9 a los 8 digitos de su numero'
            },
            direccion:{
                required:'Se necesita su direccion de domicilio actual.'
            },
            correo:{
                required:'Se necesita un correo para contactos',
                email:'Formato no valido'
            }
        }
    })
});