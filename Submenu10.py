# elegir la mascota que desees

import libreria

def Elegir_Cocker():
    a=libreria.pedir_listas("perros.txt")
    print(a)
    print(a[0])

def Elegir_Bulldog():
    b=libreria.pedir_listas("perros.txt")
    print(b)
    print(b[1])

def Elegir_Pastor_Aleman():
    c=libreria.pedir_listas("perros.txt")
    print(c)
    print(c[2])

def Mostrar_Perros():
    opc = 0
    max = 4
    while (opc != max):
        print("################ PERROS ################")
        print("#1. Cocker                             #")
        print("#2. Bulldog                            #")
        print("#3. Pastor Aleman                      #")
        print("#4. Salir                              #")
        print("########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Cocker()
        if (opc == 2):
            Elegir_Bulldog()
        if (opc == 3):
            Elegir_Pastor_Aleman()

def Elegir_Sphynx():
    g=libreria.pedir_listas("gatos.txt")
    print(g)
    print(g[0])

def Elegir_Chartreux():
    h=libreria.pedir_listas("gatos.txt")
    print(h)
    print(h[1])

def Elegir_Devon_Rex():
    i=libreria.pedir_listas("gatos.txt")
    print(i)
    print(i[2])

def Mostrar_Gatos():
    opc = 0
    max = 4
    while (opc != max):
        print("################## GATOS ##################")
        print("#1. Sphynx                                #")
        print("#2. Chartreux                             #")
        print("#3. Devon Rex                             #")
        print("#4. Salir                                 #")
        print("###########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Sphynx()
        if (opc == 2):
            Elegir_Chartreux()
        if (opc == 3):
            Elegir_Devon_Rex()

def Elegir_Conejo():
    c=libreria.pedir_listas("otros.txt")
    print(c)
    print(c[0])

def Elegir_Tortuga():
    d=libreria.pedir_listas("otros.txt")
    print(d)
    print(d[1])

def Elegir_Peces():
    e=libreria.pedir_listas("otros.txt")
    print(e)
    print(e[2])

def Mostrar_Otros():
    opc = 0
    max = 4
    while (opc != max):
        print("############ OTROS ############")
        print("#1. Educacion                 #")
        print("#2. Tortuga                   #")
        print("#3. Peces                     #")
        print("#4. Salir                     #")
        print("###############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Conejo()
        if (opc == 2):
            Elegir_Tortuga()
        if (opc == 3):
            Elegir_Peces()

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
