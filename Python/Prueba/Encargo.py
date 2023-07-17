import numpy
import FuncionesEncargo

asientos=numpy.zeros([7,6],type(int))
FuncionesEncargo.generarAsientos(asientos)

rut=[(" ") for i in range(42)]

band=False
solicitud=1

while solicitud!=6:
    print("""       
        ******* Alitas De Murcielago ^v^******
                1. Mostrar Asientos Disponibles	
                2. Comprar Pasaje
                3. Totales
                4. Anular Venta
                5. Lista De Pasajeros
                6. Salir""")

    solicitud= FuncionesEncargo.validacionRango("Ingrese una opcion: ",1,6)

    if solicitud==1:
        FuncionesEncargo.mostrarAsientos(asientos)
        band=True

    if band==True:
        if solicitud==2:
            llave=0
            FuncionesEncargo.mostrarAsientos(asientos)
            print("\n")
            solicitudAsiento=FuncionesEncargo.validacionRango("Seleccione un asiento:",1,42)
                
            if FuncionesEncargo.disponibilidadAsiento(asientos,solicitudAsiento):

                solicitudRut=FuncionesEncargo.validacionRut("Ingrese el rut del pasajero: ",8)
                rut.insert(solicitudAsiento,solicitudRut)
      
                print("Usted Selecciono el asiento:",solicitudAsiento)
                print("el precio es: $" + str(FuncionesEncargo.preciosAsientos(asientos,solicitudAsiento)))
                FuncionesEncargo.asignarAsiento(asientos,solicitudAsiento)
            else:
                print("El asiento no esta disponible")
            
        if solicitud==3:
            FuncionesEncargo.asientosVendidos(asientos)

        if solicitud==4:
            asientoPasajero=FuncionesEncargo.validacionRango("Ingrese el asiento a dejar disponible: ",1,42)
            
            if FuncionesEncargo.disponibilidadAsiento(asientos,asientoPasajero)==1:
                print("Error... el asiento se encuentra disponible")
            else:
                FuncionesEncargo.anularVenta(asientos,asientoPasajero)
                FuncionesEncargo.eliminarRut(rut,asientoPasajero)
                print("El asiento a quedado disponible y el rut eliminado de la lista de pasajeros")

        if solicitud==5:
            print("Lista de pasajeros")

            nuevalistaPasajeros = [i for i in rut if i!=" "]

            if len(nuevalistaPasajeros)==0:
                print("No se registran pasajeros")
            else:
                nuevalistaPasajeros.sort()
                print('\n'.join(map(str, nuevalistaPasajeros)))