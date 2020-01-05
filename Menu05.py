# mostrar lo que hay de canales en Directv segun tus gustos

import libreria

def Mostrar_Noticias():
    a=libreria.pedir_listas("noticias.txt")
    print("Los canales de noticias son:", a)

def Mostrar_Deportes():
    b=libreria.pedir_listas("deportes.txt")
    print("Los canales de deportes son:", b)

def Mostrar_Entretenimiento():
    c=libreria.pedir_listas("entretenimiento.txt")
    print("Los canales de entretenimiento son:", c)

opc=0
max=4
while(opc!=max):
    print("########## DIRECTV ##########")
    print("#1. Noticias                #")
    print("#2. Deportes                #")
    print("#3. Entretenimiento         #")
    print("#4. Apagar                  #")
    print("#############################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Noticias()
    if (opc==2):
        Mostrar_Deportes()
    if (opc==3):
        Mostrar_Entretenimiento()

print("Apagar la Television")
