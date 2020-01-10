# mostrar los ejemplos de cada estado

import libreria

def Mostrar_Hielo():
    a=libreria.pedir_listas("solidos.txt")
    print(a)
    print(a[0])

def Mostrar_Piedra():
    b=libreria.pedir_listas("solidos.txt")
    print(b)
    print(b[1])

def Mostrar_Hueso():
    c=libreria.pedir_listas("solidos.txt")
    print(c)
    print(c[2])

def EJM_Solidos():
    opc = 0
    max = 4
    while (opc != max):
        print("################ SOLIDOS ################")
        print("#1. Hielo                               #")
        print("#2. Piedra                              #")
        print("#3. Hueso                               #")
        print("#4. Salir                               #")
        print("#########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Mostrar_Hielo()
        if (opc == 2):
            Mostrar_Piedra()
        if (opc == 3):
            Mostrar_Hueso()

def Mostrar_Agua():
    g=libreria.pedir_listas("liquido.txt")
    print(g)
    print(g[0])

def Mostrar_Mercurio():
    h=libreria.pedir_listas("liquido.txt")
    print(h)
    print(h[1])

def Mostrar_Sangre():
    i=libreria.pedir_listas("liquido.txt")
    print(i)
    print(i[2])

def EJM_Liquido():
    opc = 0
    max = 4
    while (opc != max):
        print("################## LIQUIDO ##################")
        print("#1. Agua                                    #")
        print("#2. Mercurio                                #")
        print("#3. Sangre                                  #")
        print("#4. Salir                                   #")
        print("#############################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Mostrar_Agua()
        if (opc == 2):
            Mostrar_Mercurio()
        if (opc == 3):
            Mostrar_Sangre()

def Mostrar_Aire():
    c=libreria.pedir_listas("gaseoso.txt")
    print(c)
    print(c[0])

def Mostrar_Nitrogeno():
    d=libreria.pedir_listas("gaseoso.txt")
    print(d)
    print(d[1])

def Mostrar_Helio():
    e=libreria.pedir_listas("gaseoso.txt")
    print(e)
    print(e[2])

def EJM_Gaseoso():
    opc = 0
    max = 4
    while (opc != max):
        print("############ GASEOSO ############")
        print("#1. Aire                        #")
        print("#2. Nitrogeno                   #")
        print("#3. Helio                       #")
        print("#4. Salir                       #")
        print("#################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Mostrar_Aire()
        if (opc == 2):
            Mostrar_Nitrogeno()
        if (opc == 3):
            Mostrar_Helio()

opc=0
max=4
while(opc!=max):
    print("########## ESTADOS DE LA MATERIA ##########")
    print("#1. Solidos                               #")
    print("#2. Liquidos                              #")
    print("#3. Gaseoso                               #")
    print("#4. Salir                                 #")
    print("###########################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        EJM_Solidos()
    if (opc==2):
        EJM_Liquido()
    if (opc==3):
        EJM_Gaseoso()

print("Fin del programa")
