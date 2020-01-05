# mostrar lo que hay en una tienda de ropa

import libreria

def Mostrar_Camisas():
    a=libreria.pedir_listas("camisas.txt")
    print("Los tipos de camisas", a)

def Mostrar_Pantalones():
    b=libreria.pedir_listas("pantalon.txt")
    print("Los tipos de panalones", b)

def Mostrar_Casacas():
    c=libreria.pedir_listas("casacas.txt")
    print("Los tipos de casacas", c)

opc=0
max=4
while(opc!=max):
    print("########## TIENDA DE ROPA ##########")
    print("#1. Camisas                        #")
    print("#2. Pantalones                     #")
    print("#3. Casacas                        #")
    print("#4. Salir                          #")
    print("####################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Camisas()
    if (opc==2):
        Mostrar_Pantalones()
    if (opc==3):
        Mostrar_Casacas()

print("Salir de la Tienda")
