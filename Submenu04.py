# elegir lo que quieras en la sala de juegos

import libreria

def Elegir_Rayuela():
    a=libreria.pedir_listas("tradicionales.txt")
    print(a[0])

def Elegir_Comba():
    b=libreria.pedir_listas("tradicionales.txt")
    print(b[1])

def Elegir_Escondite():
    c=libreria.pedir_listas("tradicionales.txt")
    print(c[2])

def Mostrar_Juegos_Tradicionales():
    opc = 0
    max = 4
    while (opc != max):
        print("########## JUEGOS TRADICIONALES ##########")
        print("#1. Rayuela                              #")
        print("#2. Comba                                #")
        print("#3. Escondite                            #")
        print("#4. Salir                                #")
        print("##########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Rayuela()
        if (opc == 2):
            Elegir_Comba()
        if (opc == 3):
            Elegir_Escondite()

def Elegir_Pacman():
    d=libreria.pedir_listas("videojuegos.txt")
    print(d[1])

def Elegir_Mortal_Kombat():
    e=libreria.pedir_listas("videojuegos.txt")
    print(e[3])

def Elegir_Super_Mario_World():
    f=libreria.pedir_listas("videojuegos.txt")
    print(f[4])

def Mostrar_Videojuegos_90():
    opc = 0
    max = 4
    while (opc != max):
        print("########## VIDEOJUEGOS DE LOS 90,S ##########")
        print("#1. Pacman                                  #")
        print("#2. Mortal Kombat                           #")
        print("#3. Super Mario World                       #")
        print("#4. Salir                                   #")
        print("#############################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Pacman()
        if (opc == 2):
            Elegir_Mortal_Kombat()
        if (opc == 3):
            Elegir_Super_Mario_World()

def Elegir_Resident_Evil():
    g=libreria.pedir_listas("actuales.txt")
    print(g[0])

def Elegir_Anthem():
    h=libreria.pedir_listas("actuales.txt")
    print(h[2])

def Elegir_Jump_Force():
    i=libreria.pedir_listas("actuales.txt")
    print(i[4])

def Mostrar_Videojuegos_Actuales():
    opc = 0
    max = 4
    while (opc != max):
        print("########## VIDEOJUEGOS ACTUALES ##########")
        print("#1. Resident Evil                        #")
        print("#2. Anthem                               #")
        print("#3. Jump Force                           #")
        print("#4. Salir                                #")
        print("##########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Resident_Evil()
        if (opc == 2):
            Elegir_Anthem()
        if (opc == 3):
            Elegir_Jump_Force()

opc=0
max=4
while(opc!=max):
    print("########## SALA DE JUEGOS ##########")
    print("#1. Juegos Tradicionales           #")
    print("#2. Videojuegos de los 90's        #")
    print("#3. Videojuegos actuales           #")
    print("#4. Salir                          #")
    print("####################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Juegos_Tradicionales()
    if (opc==2):
        Mostrar_Videojuegos_90()
    if (opc==3):
        Mostrar_Videojuegos_Actuales()

print("Fin del Programa")
