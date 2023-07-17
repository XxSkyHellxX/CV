def generarAsientos(asientos):
    cont=1
    for i in range(7):
        for j in range(6):
            asientos[i][j]=cont
            cont+=1

def validacionRango(solicitud,inicio,final):
    while True:
        try:
            op=int(input(solicitud))
            if op>=inicio and op<=final:
                break
            else:
                print("Ingrese un valor entre",inicio,"-",final)
        except ValueError:
            print("tipo de dato no valido".upper())  

    return op       

def mostrarAsientos(asientos):
    for i in range(10):
            print("|\n|\t                 \t\t    |")
            if (i==5):
                print("|___________________________________________|") 
                print("|___________________________________________|")

            print("",end="| ")
            for j in range(10):
                mostrar=asientos[i][j]
                if (len(str(asientos[i][j]))==1):
                    mostrar=str(mostrar)+" "

                if (j==2):
                    print(mostrar,end="          ")
                else:
                    print(mostrar,end="    ")

def validacionRut (solicitud,largo):
    while True:
        try:
            Rut=int(input(solicitud))
            if (len(str(Rut)))==largo:
                break
            else:
                print("Ingrese el rut sin puntos ni digito verificador")
        except ValueError:
                print("tipo de dato no valido".upper())

    return Rut

def asignarAsiento(asientos,solicitud):
    for i in range(7):
        for j in range(6):
            puestos=asientos[i][j]
            if puestos==solicitud:
                asientos[i][j]="X"

def disponibilidadAsiento(asientos,solicitud):
    band=0
    for i in range(7):
        for j in range(6):
            if asientos[i][j]==solicitud:
                band=1
    return band                                

def preciosAsientos(asientos,solicitud):
    precio=0
    for i in range(7):
        for j in range(6):
            if asientos[i][j]==solicitud:
                if asientos[i][j]>=31 and asientos[i][j]<=42:
                    precio=250000
                else:
                    precio=75000    
    return precio

def asientosVendidos(asientosVendidos):
    cont=0
    contVIP=0
    contNORM=0
    suma=0
    for i in range(7):
        for j in range(6):
            cont+=1
            if str(asientosVendidos[i][j])=="X":
                if cont<31:
                    contNORM+=1
                    suma+=75000
                else:
                    contVIP+=1
                    suma+=250000
    
    print("Cantidad de asientos VIP vendidos=>",contVIP)
    print("Cantidad de asientos normales vendidos=>",contNORM)
    print("El total vendido es: $" + str(suma))

    return suma                

def anularVenta(asientos,solicitud):
    cont=1
    for i in range(7):
        for j in range(6):
            if solicitud==cont:
                asientos[i][j]=solicitud
            cont+=1

def eliminarRut(rut,solicitud):
    rut.pop(solicitud)