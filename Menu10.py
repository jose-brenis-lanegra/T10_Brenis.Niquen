# mostrar lo que hay en una tienda de mascotas

import libreria

def Mostrar_Perros():
    a=libreria.pedir_listas("perros.txt")
    print("Las razas de perros que hay son:")
    print(a)

def Mostrar_Gatos():
    b=libreria.pedir_listas("gatos.txt")
    print("Las razas de gatos que hay son:")
    print(b)

def Mostrar_Otros():
    c=libreria.pedir_listas("otros.txt")
    print("Las otras mascotas son:")
    print(c)

opc=0
max=4
while(opc!=max):
    print("########## TIENDA DE MASCOTA ##########")
    print("#1. Perros                            #")
    print("#2. Gatos                             #")
    print("#3. Otros                             #")
    print("#4. Salir                             #")
    print("#######################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Perros()
    if (opc==2):
        Mostrar_Gatos()
    if (opc==3):
        Mostrar_Otros()

print("salir de la tienda")
