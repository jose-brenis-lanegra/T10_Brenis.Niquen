# elegir el medicamento que necesites

import libreria

def Elegir_Dextrometorfano():
    a=libreria.pedir_listas("tos.txt")
    print(a)
    print(a[0])

def Elegir_Ibuprofeno():
    b=libreria.pedir_listas("tos.txt")
    print(b)
    print(b[1])

def Elegir_Paracetamol():
    c=libreria.pedir_listas("tos.txt")
    print(c)
    print(c[2])

def Mostrar_Para_Tos():
    opc = 0
    max = 4
    while (opc != max):
        print("########## MEDICAMENTO PARA LA TOS ##########")
        print("#1. Dextrometorfano                         #")
        print("#2. Ibuprofeno                              #")
        print("#3. Paracetamol                             #")
        print("#4. Salir                                   #")
        print("#############################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Dextrometorfano()
        if (opc == 2):
            Elegir_Ibuprofeno()
        if (opc == 3):
            Elegir_Paracetamol()

def Elegir_Dipirona():
    d=libreria.pedir_listas("fiebre.txt")
    print(d)
    print(d[0])

def Elegir_Asprina():
    e=libreria.pedir_listas("fiebre.txt")
    print(e)
    print(e[1])

def Elegir_Amoxicilina():
    f=libreria.pedir_listas("fiebre.txt")
    print(f)
    print(f[2])

def Mostrar_Para_Fiebre():
    opc = 0
    max = 4
    while (opc != max):
        print("########## MEDICAMENTO PARA LA FIEBRE ##########")
        print("#1. Dipirona                                   #")
        print("#2. Asprina                                    #")
        print("#3. Amoxicilina                                #")
        print("#4. Salir                                      #")
        print("################################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Dipirona()
        if (opc == 2):
            Elegir_Asprina()
        if (opc == 3):
            Elegir_Amoxicilina()

def Elegir_Cetirizina():
    g=libreria.pedir_listas("alergia.txt")
    print(g)
    print(g[0])

def Elegir_Desloratadina():
    h=libreria.pedir_listas("alergia.txt")
    print(h)
    print(h[1])

def Elegir_Fexofenadina():
    i=libreria.pedir_listas("alergia.txt")
    print(i)
    print(i[2])

def Mostrar_Para_Alergia():
    opc = 0
    max = 4
    while (opc != max):
        print("########## MEDICAMENTO PARA LA ALERGIA ##########")
        print("#1. Cetirizina                                  #")
        print("#2. Desloratadina                               #")
        print("#3. Fexofenadina                                #")
        print("#4. Salir                                       #")
        print("#################################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Cetirizina()
        if (opc == 2):
            Elegir_Desloratadina()
        if (opc == 3):
            Elegir_Fexofenadina()

opc=0
max=4
while(opc!=max):
    print("########## FARMACIA ##########")
    print("#1. Para la Tos              #")
    print("#2. Para la Fiebre           #")
    print("#3. Para la Alergia          #")
    print("#4. Salir                    #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Para_Tos()
    if (opc==2):
        Mostrar_Para_Fiebre()
    if (opc==3):
        Mostrar_Para_Alergia()

print("Salir de la Farmacia")
