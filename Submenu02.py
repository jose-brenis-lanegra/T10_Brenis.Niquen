# elegir lo que quieras en la tienda

import libreria

def Elegir_Manzana():
    a=libreria.pedir_listas("frutas.txt")
    print(a[0])

def Elegir_Naranja():
    b=libreria.pedir_listas("frutas.txt")
    print(b[1])

def Elegir_Uva():
    c=libreria.pedir_listas("frutas.txt")
    print(c[2])

def Mostrar_Frutas():
    opc = 0
    max = 4
    while (opc != max):
        print("########## FRUTAS ##########")
        print("#1. Manzana                #")
        print("#2. Naranja                #")
        print("#3. Uva                    #")
        print("#4. Salir                  #")
        print("############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Manzana()
        if (opc == 2):
            Elegir_Naranja()
        if (opc == 3):
            Elegir_Uva()

def Elegir_Tomate():
    d=libreria.pedir_listas("verduras.txt")
    print(d[2])

def Elegir_Beteraga():
    e=libreria.pedir_listas("verduras.txt")
    print(e[3])

def Elegir_Pepinos():
    f=libreria.pedir_listas("verduras.txt")
    print(f[4])

def Mostrar_Verduras():
    opc = 0
    max = 4
    while (opc != max):
        print("########## VERDURAS ##########")
        print("#1. Tomate                   #")
        print("#2. Beteraga                 #")
        print("#3. Pepinos                  #")
        print("#4. Salir                    #")
        print("##############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Tomate()
        if (opc == 2):
            Elegir_Beteraga()
        if (opc == 3):
            Elegir_Pepinos()

def Elegir_Trigo():
    g=libreria.pedir_listas("harinas.txt")
    print(g[1])

def Elegir_Avena():
    h=libreria.pedir_listas("harinas.txt")
    print(h[2])

def Elegir_Pasta():
    i=libreria.pedir_listas("harinas.txt")
    print(i[3])

def Mostrar_Harinas():
    opc = 0
    max = 4
    while (opc != max):
        print("########## HARINAS ##########")
        print("#1. Trigo                   #")
        print("#2. Avena                   #")
        print("#3. Pasta                   #")
        print("#4. Salir                   #")
        print("#############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Trigo()
        if (opc == 2):
            Elegir_Avena()
        if (opc == 3):
            Elegir_Pasta()

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

print("Salir de la Tienda")
