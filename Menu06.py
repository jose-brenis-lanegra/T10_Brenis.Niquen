# mostrar lo que hay en una farmacia

import libreria

def Mostrar_Para_Tos():
    a=libreria.pedir_listas("tos.txt")
    print("Para la Tos son:", a)

def Mostrar_Para_Fiebre():
    b=libreria.pedir_listas("fiebre.txt")
    print("Para la Fiebre son:", b)

def Mostrar_Para_Alergia():
    c=libreria.pedir_listas("alergia.txt")
    print("Para la Alergia son:", c)

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
