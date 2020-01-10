# ejemplos de los estados de la materia

import libreria

def EJM_Solidos():
    a=libreria.pedir_listas("solidos.txt")
    print("ejemplos del estado solido:")
    print(a)

def EJM_Liquido():
    b=libreria.pedir_listas("liquido.txt")
    print("ejemplos del estado liquido:")
    print(b)

def EJM_Gaseoso():
    c=libreria.pedir_listas("gaseoso.txt")
    print("ejemplos del estado gaseoso:")
    print(c)

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
