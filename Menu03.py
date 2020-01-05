#mostrar lo que hay en la Panderia segun lo que quieres
import libreria

def Mostrar_Panes():
    a=libreria.pedir_listas("panes.txt")
    print("Los Panes", a)

def Mostrar_Tortas():
    b=libreria.pedir_listas("tortas.txt")
    print("Las Tortas", b)

def Mostrar_Postres():
    c=libreria.pedir_listas("postres.txt")
    print("Los Postres", c)

opc=0
max=4
while(opc!=max):
    print("########## PANADERIA ##########")
    print("#1. Panes                     #")
    print("#2. Tortas                    #")
    print("#3. Postres                   #")
    print("#4. Salir                     #")
    print("###############################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if (opc==1):
        Mostrar_Panes()
    if (opc==2):
        Mostrar_Tortas()
    if (opc==3):
        Mostrar_Postres()

print("Salir de la Panaderia")
