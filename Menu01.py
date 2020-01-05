# mostrar lo que hay en una tienda segun lo que pidas
import libreria

def Mostrar_Frutas():
    a=libreria.pedir_listas("frutas.txt")
    print("Las Frutas", a)

def Mostrar_Verduras():
    b=libreria.pedir_listas("verduras.txt")
    print("Las Verduras", b)

def Mostrar_Harinas():
    c=libreria.pedir_listas("harinas.txt")
    print("Las Harinas", c)

opc=0
max=4
while(opc!=max):
    print("########## TIENDA ##########")
    print("#1. Frutas                 #")
    print("#2. Verduras               #")
    print("#3. Harinas                #")
    print("#4. Salir                  #")
    print("############################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Frutas()
    if (opc==2):
        Mostrar_Verduras()
    if (opc==3):
        Mostrar_Harinas()

print("salir de la tienda")
