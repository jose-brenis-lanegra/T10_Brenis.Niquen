# elege la escuela en que quieres estudiar

import libreria

def Elegir_Agronomia():
    a=libreria.pedir_listas("fag.txt")
    print(a)

def Mostrar_FAG():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FAG ##########")
        print("#1. Agronomia           #")
        print("#2. Salir               #")
        print("#########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Agronomia()

def Elegir_Biologia():
    b=libreria.pedir_listas("fccbb.txt")
    print(b)

def Mostrar_FCCBB():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FCCBB ##########")
        print("#1. Biologia             #")
        print("#2. Salir                #")
        print("##########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Biologia()

def Elegir_Contabilidad():
    c=libreria.pedir_listas("faceac.txt")
    print(c)
    print(c[0])

def Elegir_Economia():
    d=libreria.pedir_listas("faceac.txt")
    print(d)
    print(d[1])

def Elegir_Administracion():
    e=libreria.pedir_listas("faceac.txt")
    print(e)
    print(e[2])

def Elegir_Comercio():
    f=libreria.pedir_listas("faceac.txt")
    print(f)
    print(f[3])

def Mostrar_FACEAC():
    opc = 0
    max = 5
    while (opc != max):
        print("################ FACEAC ################")
        print("#1. Contabilidad                       #")
        print("#2. Economia                           #")
        print("#3. Administracion                     #")
        print("#4. Comercio y Negocios Internacionales#")
        print("#5. Salir                              #")
        print("########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 5)

        if (opc == 1):
            Elegir_Contabilidad()
        if (opc == 2):
            Elegir_Economia()
        if (opc == 3):
            Elegir_Administracion()
        if (opc == 4):
            Elegir_Comercio()

def Elegir_Fisica():
    g=libreria.pedir_listas("facfym.txt")
    print(g)
    print(g[0])

def Elegir_Matematicas():
    h=libreria.pedir_listas("facfym.txt")
    print(h)
    print(h[1])

def Elegir_Estadistica():
    i=libreria.pedir_listas("facfym.txt")
    print(i)
    print(i[2])

def Elegir_Informatica():
    a=libreria.pedir_listas("facfym.txt")
    print(a)
    print(a[3])

def Elegir_Electronica():
    b=libreria.pedir_listas("facfym.txt")
    print(b)
    print(b[4])

def Mostrar_FACFYM():
    opc = 0
    max = 6
    while (opc != max):
        print("################## FACFYM ##################")
        print("#1. Fisica                                 #")
        print("#2. Matematicas                            #")
        print("#3. Estadistica                            #")
        print("#4. Ingeniería de Computación e Informática#")
        print("#5. Ingeniería Electrónica                 #")
        print("#6. Salir                                  #")
        print("############################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 6)

        if (opc == 1):
            Elegir_Fisica()
        if (opc == 2):
            Elegir_Matematicas()
        if (opc == 3):
            Elegir_Estadistica()
        if (opc == 4):
            Elegir_Informatica()
        if (opc == 5):
            Elegir_Electronica()

def Elegir_Educacion():
    c=libreria.pedir_listas("fachse.txt")
    print(c)
    print(c[0])

def Elegir_Sociologia():
    d=libreria.pedir_listas("fachse.txt")
    print(d)
    print(d[1])

def Elegir_Comunicacion():
    e=libreria.pedir_listas("fachse.txt")
    print(e)
    print(e[2])

def Elegir_Psicologia():
    f=libreria.pedir_listas("fachse.txt")
    print(f)
    print(f[3])

def Elegir_Arte():
    g=libreria.pedir_listas("fachse.txt")
    print(g)
    print(g[4])

def Elegir_Arqueologia():
    h=libreria.pedir_listas("fachse.txt")
    print(h)
    print(h[5])

def Mostrar_FACHSE():
    opc = 0
    max = 7
    while (opc != max):
        print("############ FACHSE ############")
        print("#1. Educacion                  #")
        print("#2. Sociologia                 #")
        print("#3. Ciencias de la Comunicacion#")
        print("#4. Psicologia                 #")
        print("#5. Arte                       #")
        print("#6. Arqueologia                #")
        print("#7. Salir                      #")
        print("################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 7)

        if (opc == 1):
            Elegir_Educacion()
        if (opc == 2):
            Elegir_Sociologia()
        if (opc == 3):
            Elegir_Comunicacion()
        if (opc == 4):
            Elegir_Psicologia()
        if (opc == 5):
            Elegir_Arte()
        if (opc == 6):
            Elegir_Arqueologia()

def Elegir_Derecho():
    i=libreria.pedir_listas("fdccpp.txt")
    print(i)
    print(i[0])

def Elegir_Politica():
    a=libreria.pedir_listas("fdccpp.txt")
    print(a)
    print(a[1])

def Mostrar_FDCCPP():
    opc = 0
    max = 3
    while (opc != max):
        print("########## FDCCPP ##########")
        print("#1. Derecho                #")
        print("#2. Ciencia Politica       #")
        print("#3. Salir                  #")
        print("############################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 3)

        if (opc == 1):
            Elegir_Derecho()
        if (opc == 2):
            Elegir_Politica()

def Elegir_Enfermeria():
    b=libreria.pedir_listas("fe.txt")
    print(b)

def Mostrar_FE():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FE ##########")
        print("#1. Enfermeria         #")
        print("#2. Salir              #")
        print("########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Enfermeria()

def Elegir_Agricola():
    c=libreria.pedir_listas("fia.txt")
    print(c)

def Mostrar_FIA():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FIA ##########")
        print("#1. Ingenieria Agricola #")
        print("#2. Salir               #")
        print("#########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Agricola()

def Elegir_Civil():
    d=libreria.pedir_listas("ficsa.txt")
    print(d)
    print(d[0])

def Elegir_Arquitectura():
    e=libreria.pedir_listas("ficsa.txt")
    print(e)
    print(e[1])

def Elegir_Sistemas():
    f=libreria.pedir_listas("ficsa.txt")
    print(f)
    print(f[2])

def Mostrar_FICSA():
    opc = 0
    max = 4
    while (opc != max):
        print("########## FICSA ##########")
        print("#1. Ingenieria Civil      #")
        print("#2. Arquitectura          #")
        print("#3. Ingenieria de Sistemas#")
        print("#4. Salir                 #")
        print("###########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            Elegir_Civil()
        if (opc == 2):
            Elegir_Arquitectura()
        if (opc == 3):
            Elegir_Sistemas()

def Elegir_Mecanica_Electrica():
    g=libreria.pedir_listas("fime.txt")
    print(g)

def Mostrar_FIME():
    opc = 0
    max = 2
    while (opc != max):
        print("############### FIME ###############")
        print("#1. Ingenieria Mecanica y Electrica#")
        print("#2. Salir                          #")
        print("####################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Mecanica_Electrica()

def Elegir_Humana():
    h=libreria.pedir_listas("fmh.txt")
    print(h)

def Mostrar_FMH():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FMH ##########")
        print("#1. Medicina Humana     #")
        print("#2. Salir               #")
        print("#########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Humana()

def Elegir_Veterinaria():
    i=libreria.pedir_listas("fmv.txt")
    print(i)

def Mostrar_FMV():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FMV ##########")
        print("#1. Medicina Veterinaria#")
        print("#2. Salir               #")
        print("#########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Veterinaria()

def Elegir_Quimica():
    i=libreria.pedir_listas("fiquia.txt")
    print(i)
    print(i[0])

def Elegir_Industrias():
    a=libreria.pedir_listas("fiquia.txt")
    print(a)
    print(a[1])

def Mostrar_FIQUIA():
    opc = 0
    max = 3
    while (opc != max):
        print("################# FIQUIA #################")
        print("#1. Ingenieria Quimica                   #")
        print("#2. Ingenieria en Industrias Alimentarias#")
        print("#3. Salir                                #")
        print("##########################################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 3)

        if (opc == 1):
            Elegir_Quimica()
        if (opc == 2):
            Elegir_Industrias()

def Elegir_Zootecnia():
    i=libreria.pedir_listas("fiz.txt")
    print(i)

def Mostrar_FIZ():
    opc = 0
    max = 2
    while (opc != max):
        print("########## FIZ ##########")
        print("#1. Zootecnia           #")
        print("#2. Salir               #")
        print("#########################")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 2)

        if (opc == 1):
            Elegir_Zootecnia()

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
