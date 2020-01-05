# elegir lo que quieras en la tienda de ropa

import libreria

def Elegir_Sport():
    a=libreria.pedir_listas("camisas.txt")
    print(a[0])

def Elegir_De_Vestir():
    b=libreria.pedir_listas("camisas.txt")
    print(b[1])

def Elegir_Guanabera():
    c=libreria.pedir_listas("camisas.txt")
    print(c[2])

def Mostrar_Camisas():
    opc = 0
    max = 4
    while (opc != max):
        print("########## CAMISAS ##########")
        print("#1. Sport                   #")
        print("#2. De Vestir               #")
        print("#3. Guanabera               #")
        print("#4. Salir                   #")
        print("#############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Sport()
        if (opc == 2):
            Elegir_De_Vestir()
        if (opc == 3):
            Elegir_Guanabera()

def Elegir_Cropped_Rojo():
    d=libreria.pedir_listas("pantalon.txt")
    print(d[0])

def Elegir_Corte_Pitillo():
    e=libreria.pedir_listas("pantalon.txt")
    print(e[1])

def Elegir_Corte_Recto():
    f=libreria.pedir_listas("pantalon.txt")
    print(f[2])

def Mostrar_Pantalones():
    opc = 0
    max = 4
    while (opc != max):
        print("########## PANTALONES ##########")
        print("#1. Cropped Rojo               #")
        print("#2. Corte Pitillo              #")
        print("#3. Corte Recto                #")
        print("#4. Salir                      #")
        print("################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Cropped_Rojo()
        if (opc == 2):
            Elegir_Corte_Pitillo()
        if (opc == 3):
            Elegir_Corte_Recto()

def Elegir_Americana():
    g=libreria.pedir_listas("casacas.txt")
    print(g[0])

def Elegir_Bomber():
    h=libreria.pedir_listas("casacas.txt")
    print(h[2])

def Elegir_Husky():
    i=libreria.pedir_listas("casacas.txt")
    print(i[4])

def Mostrar_Casacas():
    opc = 0
    max = 4
    while (opc != max):
        print("########## CASACAS ##########")
        print("#1. Americana               #")
        print("#2. Bomber                  #")
        print("#3. Husky                   #")
        print("#4. Salir                   #")
        print("#############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Americana()
        if (opc == 2):
            Elegir_Bomber()
        if (opc == 3):
            Elegir_Husky()

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
