# elegir lo que quieras en la tienda

import libreria

def Elegir_Pan_Caracol():
    a=libreria.pedir_listas("panes.txt")
    print(a[0])

def Elegir_Pan_Pizza():
    b=libreria.pedir_listas("panes.txt")
    print(b[1])

def Elegir_Pan_Molde():
    c=libreria.pedir_listas("panes.txt")
    print(c[3])

def Mostrar_Panes():
    opc = 0
    max = 4
    while (opc != max):
        print("########## PANES ##########")
        print("#1. Pan Caracol           #")
        print("#2. Pan Pizza             #")
        print("#3. Pan Molde             #")
        print("#4. Salir                 #")
        print("###########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Pan_Caracol()
        if (opc == 2):
            Elegir_Pan_Pizza()
        if (opc == 3):
            Elegir_Pan_Molde()

def Elegir_Torta_De_Naranja():
    d=libreria.pedir_listas("tortas.txt")
    print(d[1])

def Elegir_Torta_Helada():
    e=libreria.pedir_listas("tortas.txt")
    print(e[2])

def Elegir_Torta_De_Pina():
    f=libreria.pedir_listas("tortas.txt")
    print(f[4])

def Mostrar_Tortas():
    opc = 0
    max = 4
    while (opc != max):
        print("########## TORTAS ##########")
        print("#1. Torta de Naranja       #")
        print("#2. Torta Helada           #")
        print("#3. Torta de Piña          #")
        print("#4. Salir                   #")
        print("#############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Torta_De_Naranja()
        if (opc == 2):
            Elegir_Torta_Helada()
        if (opc == 3):
            Elegir_Torta_De_Pina()

def Elegir_Pionono():
    g=libreria.pedir_listas("postres.txt")
    print(g[2])

def Elegir_Mazamorra():
    h=libreria.pedir_listas("postres.txt")
    print(h[3])

def Elegir_Budin():
    i=libreria.pedir_listas("postres.txt")
    print(i[4])

def Mostrar_Postres():
    opc = 0
    max = 4
    while (opc != max):
        print("########## POSTRES ##########")
        print("#1. Pionono                 #")
        print("#2. Mazamorra               #")
        print("#3. Budin                   #")
        print("#4. Salir                   #")
        print("#############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Pionono()
        if (opc == 2):
            Elegir_Mazamorra()
        if (opc == 3):
            Elegir_Budin()

opc=0
max=4
while(opc!=max):
    print("########## PANADERIA ##########")
    print("#1. Panes                     #")
    print("#2. Tortas                    #")
    print("#3. Postres                   #")
    print("#4. Salir                     #")
    print("###############################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Panes()
    if (opc==2):
        Mostrar_Tortas()
    if (opc==3):
        Mostrar_Postres()

print("Salir de la Panaderia")
