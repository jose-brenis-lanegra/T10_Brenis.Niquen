#mostrar los juegos que hay en una sala de juegos segun tus gustos
import libreria

def Mostrar_Juegos_Tradicionales():
    a=libreria.pedir_listas("tradicionales.txt")
    print("Los Juegos Tradicionales", a)

def Mostrar_Videojuegos_90():
    b=libreria.pedir_listas("videojuegos.txt")
    print("Los Videojuegos", b)

def Mostrar_Videojuegos_actuales():
    c=libreria.pedir_listas("actuales.txt")
    print("Los juegos virtuales", c)

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
        Mostrar_Videojuegos_actuales()

print("Fin del Programa")
