#mostrar algunos electrodomesticos de cada clase

import libreria

def Mostrar_Linea_Marron():
    a=libreria.pedir_listas("marron.txt")
    print("Los Electrodomesticos de Linea Marron son:", a)

def Mostrar_Linea_Blanca():
    b=libreria.pedir_listas("blanca.txt")
    print("Los Electrodomesticos de Linea Blanca son:", b)

def Mostrar_Etiqueta_Energetica():
    c=libreria.pedir_listas("etiqueta.txt")
    print("Los Los Electrodomesticos de Etiqueta Energetica son:", c)

opc=0
max=4
while(opc!=max):
    print("########## ELECTRODOMESTICOS ##########")
    print("#1. Linea Marron                      #")
    print("#2. Linea Blanca                      #")
    print("#3. Etiqueta Energetica               #")
    print("#4. Salir                             #")
    print("#######################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Linea_Marron()
    if (opc==2):
        Mostrar_Linea_Blanca()
    if (opc==3):
        Mostrar_Etiqueta_Energetica()

print("Fin del Programa")
