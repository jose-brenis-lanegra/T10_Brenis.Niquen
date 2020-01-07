# elegir el elecrodomestico que quieres

import libreria

def Elegir_Televisor():
    a=libreria.pedir_listas("marron.txt")
    print(a)
    print(a[0])

def Elegir_Reproductor_DVD():
    b=libreria.pedir_listas("marron.txt")
    print(b)
    print(b[1])

def Elegir_Computadora():
    c=libreria.pedir_listas("marron.txt")
    print(c)
    print(c[2])

def Mostrar_Linea_Marron():
    opc = 0
    max = 4
    while (opc != max):
        print("########## LINEA MARRON ##########")
        print("#1. Televisor                    #")
        print("#2. Reproductor de DVD           #")
        print("#3. Computadora                  #")
        print("#4. Salir                        #")
        print("##################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Televisor()
        if (opc == 2):
            Elegir_Reproductor_DVD()
        if (opc == 3):
            Elegir_Computadora()

def Elegir_Microondas():
    d=libreria.pedir_listas("blanca.txt")
    print(d)
    print(d[0])

def Elegir_Nevera():
    e=libreria.pedir_listas("blanca.txt")
    print(e)
    print(e[1])

def Elegir_Secarropas():
    f=libreria.pedir_listas("blanca.txt")
    print(f)
    print(f[2])

def Mostrar_Linea_Blanca():
    opc = 0
    max = 4
    while (opc != max):
        print("########## LINEA BLANCA ##########")
        print("#1. Microondas                   #")
        print("#2. Nevera                       #")
        print("#3. Secarropas                   #")
        print("#4. Salir                        #")
        print("##################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Microondas()
        if (opc == 2):
            Elegir_Nevera()
        if (opc == 3):
            Elegir_Secarropas()

def Elegir_Horno_Electrico():
    g=libreria.pedir_listas("etiqueta.txt")
    print(g)
    print(g[0])

def Elegir_Lavavajillas():
    h=libreria.pedir_listas("etiqueta.txt")
    print(h)
    print(h[1])

def Elegir_Secadoras():
    i=libreria.pedir_listas("etiqueta.txt")
    print(i)
    print(i[2])

def Mostrar_Etiqueta_Energetica():
    opc = 0
    max = 4
    while (opc != max):
        print("########## ETIQUETA ENERGETICA ##########")
        print("#1. Horno electrico                     #")
        print("#2. Lavavajillas                        #")
        print("#3. Secadoras                           #")
        print("#4. Salir                               #")
        print("#########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Horno_Electrico()
        if (opc == 2):
            Elegir_Lavavajillas()
        if (opc == 3):
            Elegir_Secadoras()

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
