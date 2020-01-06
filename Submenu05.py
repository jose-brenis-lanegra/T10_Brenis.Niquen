# elegir los canales q gustes de DIRECTV

import libreria

def Elegir_CNN():
    a=libreria.pedir_listas("noticias.txt")
    print(a)
    print(a[0])

def Elegir_TVPE():
    b=libreria.pedir_listas("noticias.txt")
    print(b)
    print(b[1])

def Elegir_Telesur():
    c=libreria.pedir_listas("noticias.txt")
    print(c)
    print(c[2])

def Mostrar_Noticias():
    opc = 0
    max = 4
    while (opc != max):
        print("########## NOTICIAS ##########")
        print("#1. CNN                      #")
        print("#2. TVPE                     #")
        print("#3. Telesur                  #")
        print("#4. Cambiar                  #")
        print("##############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_CNN()
        if (opc == 2):
            Elegir_TVPE()
        if (opc == 3):
            Elegir_Telesur()

def Elegir_Fox_Sports():
    d=libreria.pedir_listas("deportes.txt")
    print(d)
    print(d[0])

def Elegir_ESPN():
    e=libreria.pedir_listas("deportes.txt")
    print(e)
    print(e[1])

def Elegir_TyC_Sports():
    f=libreria.pedir_listas("deportes.txt")
    print(f)
    print(f[2])

def Mostrar_Deportes():
    opc = 0
    max = 4
    while (opc != max):
        print("########## DEPORTES ##########")
        print("#1. Fox Sports               #")
        print("#2. ESPN                     #")
        print("#3. TyC Sports               #")
        print("#4. Cambiar                  #")
        print("##############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Fox_Sports()
        if (opc == 2):
            Elegir_ESPN()
        if (opc == 3):
            Elegir_TyC_Sports()

def Elegir_FOX():
    g=libreria.pedir_listas("entretenimiento.txt")
    print(g)
    print(g[0])

def Elegir_Cartoon_Network():
    h=libreria.pedir_listas("entretenimiento.txt")
    print(h)
    print(h[1])

def Elegir_Cinemax():
    i=libreria.pedir_listas("entretenimiento.txt")
    print(i)
    print(i[2])

def Mostrar_Entretenimiento():
    opc = 0
    max = 4
    while (opc != max):
        print("########## ENTRETENIMIENTO ##########")
        print("#1. FOX                             #")
        print("#2. Cartoon Network                 #")
        print("#3. Cinemax                         #")
        print("#4. Cambiar                         #")
        print("#####################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_FOX()
        if (opc == 2):
            Elegir_Cartoon_Network()
        if (opc == 3):
            Elegir_Cinemax()

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
