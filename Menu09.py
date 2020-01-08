#mostrar las escuelas de cada facultad de la UNPRG

import libreria

def Mostrar_FAG():
    a=libreria.pedir_listas("fag.txt")
    print("Las escuelas de FAG son:")
    print(a)

def Mostrar_FCCBB():
    b=libreria.pedir_listas("fccbb.txt")
    print("Las escuelas de FCCBB son:")
    print(b)

def Mostrar_FACEAC():
    c=libreria.pedir_listas("faceac.txt")
    print("Las escuelas de FACEAC son:")
    print(c)

def Mostrar_FACFYM():
    a=libreria.pedir_listas("facfym.txt")
    print("Las escuelas de FACFYM son:")
    print(a)

def Mostrar_FACHSE():
    b=libreria.pedir_listas("fachse.txt")
    print("Las escuelas de FACHSE son:")
    print(b)

def Mostrar_FDCCPP():
    c=libreria.pedir_listas("fdccpp.txt")
    print("Las escuelas de FDCCPP son:")
    print(c)

def Mostrar_FE():
    a=libreria.pedir_listas("fe.txt")
    print("Las escuelas de FE son:")
    print(a)

def Mostrar_FIA():
    b=libreria.pedir_listas("fia.txt")
    print("Las escuelas de FIA son:")
    print(b)

def Mostrar_FICSA():
    c=libreria.pedir_listas("ficsa.txt")
    print("Las escuelas de FICSA son:")
    print(c)

def Mostrar_FIME():
    a=libreria.pedir_listas("fime.txt")
    print("Las escuelas de FIME son:")
    print(a)

def Mostrar_FMH():
    b=libreria.pedir_listas("fmh.txt")
    print("Las escuelas de FMH son:")
    print(b)

def Mostrar_FMV():
    c=libreria.pedir_listas("fmv.txt")
    print("Las escuelas de FMV son:")
    print(c)

def Mostrar_FIQUIA():
    a=libreria.pedir_listas("fiquia.txt")
    print("Las escuelas de FIQUIA son:")
    print(a)

def Mostrar_FIZ():
    b=libreria.pedir_listas("fiz.txt")
    print("Las escuelas de FIZ son:")
    print(b)

opc=0
max=15
while(opc!=max):
    print("############# UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO #############")
    print("#1. Facultad de Agronomía                                       #")
    print("#2. Facultad de Ciencias Biológicas                             #")
    print("#3. Facultad de Ciencias Económicas, Administrativas y Contables#")
    print("#4. Facultad de Ciencias Físicas y Matemáticas                  #")
    print("#5. Facultad de Ciencias Histórico Sociales y Educación         #")
    print("#6. Facultad de Derecho y Ciencias Políticas                    #")
    print("#7. Facultad de Enfermería                                      #")
    print("#8. Facultad de Ingeniería Agrícola                             #")
    print("#9. Facultad de Ingeniería Civil, de Sistemas y de Arquitectura #")
    print("#10. Facultad de Ingeniería Mecánica y Eléctrica                #")
    print("#11. Facultad de Medicina Humana                                #")
    print("#12. Facultad de Medicina Veterinaria                           #")
    print("#13. Facultad de Ingeniería Química e Industrias Alimentarias   #")
    print("#14. Facultad de Zootecnia                                      #")
    print("#15. Salir                                                      #")
    print("#################################################################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 15)

    if (opc==1):
        Mostrar_FAG()
    if (opc==2):
        Mostrar_FCCBB()
    if (opc==3):
        Mostrar_FACEAC()
    if (opc==4):
        Mostrar_FACFYM()
    if (opc==5):
        Mostrar_FACHSE()
    if (opc==6):
        Mostrar_FDCCPP()
    if (opc==7):
        Mostrar_FE()
    if (opc==8):
        Mostrar_FIA()
    if (opc==9):
        Mostrar_FICSA()
    if (opc==10):
        Mostrar_FIME()
    if (opc==11):
        Mostrar_FMH()
    if (opc==12):
        Mostrar_FMV()
    if (opc==13):
        Mostrar_FIQUIA()
    if (opc==14):
        Mostrar_FIZ()

print("Fin del programa")
