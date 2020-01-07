# mostrar algunos instrumentos musicales segun su clasificacion

import libreria

def Mostrar_Viento():
    a=libreria.pedir_listas("viento.txt")
    print("Los instrumentos de viento son:", a)

def Mostrar_Cuerda():
    b=libreria.pedir_listas("cuerda.txt")
    print("Los instrumentos de cuerda son:", b)

def Mostrar_Percusion():
    c=libreria.pedir_listas("percusion.txt")
    print("Los instrumentos de percusion son:", c)

opc=0
max=4
while(opc!=max):
    print("########## INSTRUMENTOS MUSICALES ##########")
    print("#1. De Viento                              #")
    print("#2. De Cuerda                              #")
    print("#3. De Percusion                           #")
    print("#4. Salir                                  #")
    print("############################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Viento()
    if (opc==2):
        Mostrar_Cuerda()
    if (opc==3):
        Mostrar_Percusion()

print("Fin del programa")
