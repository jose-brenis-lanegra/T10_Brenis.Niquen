# elegir el elecrodomestico que quieres

import libreria

def Elegir_Saxofon():
    a=libreria.pedir_listas("viento.txt")
    print(a)
    print(a[0])

def Elegir_Flauta():
    b=libreria.pedir_listas("viento.txt")
    print(b)
    print(b[1])

def Elegir_Oboe():
    c=libreria.pedir_listas("viento.txt")
    print(c)
    print(c[2])

def Mostrar_Viento():
    opc = 0
    max = 4
    while (opc != max):
        print("########## DE VIENTO ##########")
        print("#1. Saxofon                   #")
        print("#2. Flauta                    #")
        print("#3. Oboe                      #")
        print("#4. Salir                     #")
        print("###############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Saxofon()
        if (opc == 2):
            Elegir_Flauta()
        if (opc == 3):
            Elegir_Oboe()

def Elegir_Guitarra():
    d=libreria.pedir_listas("cuerda.txt")
    print(d)
    print(d[0])

def Elegir_Arpa():
    e=libreria.pedir_listas("cuerda.txt")
    print(e)
    print(e[1])

def Elegir_Violin():
    f=libreria.pedir_listas("cuerda.txt")
    print(f)
    print(f[2])

def Mostrar_Cuerda():
    opc = 0
    max = 4
    while (opc != max):
        print("########## DE CUERDA ##########")
        print("#1. Guitarra                  #")
        print("#2. Arpa                      #")
        print("#3. Violin                    #")
        print("#4. Salir                     #")
        print("###############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Guitarra()
        if (opc == 2):
            Elegir_Arpa()
        if (opc == 3):
            Elegir_Violin()

def Elegir_Timbal():
    g=libreria.pedir_listas("percusion.txt")
    print(g)
    print(g[0])

def Elegir_Tambor():
    h=libreria.pedir_listas("percusion.txt")
    print(h)
    print(h[1])

def Elegir_Bombo():
    i=libreria.pedir_listas("percusion.txt")
    print(i)
    print(i[2])

def Mostrar_Percusion():
    opc = 0
    max = 4
    while (opc != max):
        print("########## DE PERCUSION ##########")
        print("#1. Timbal                       #")
        print("#2. Tambor                       #")
        print("#3. Bombo                        #")
        print("#4. Salir                        #")
        print("##################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Timbal()
        if (opc == 2):
            Elegir_Tambor()
        if (opc == 3):
            Elegir_Bombo()

opc=0
max=4
while(opc!=max):
    print("########## INSTRUMENTOS MUSICALES ##########")
    print("#1. De Viento                              #")
    print("#2. De Cuerda                              #")
    print("#3. De Percusion                           #")
    print("#4. Salir                                  #")
    print("############################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Viento()
    if (opc==2):
        Mostrar_Cuerda()
    if (opc==3):
        Mostrar_Percusion()

print("Fin del programa")
