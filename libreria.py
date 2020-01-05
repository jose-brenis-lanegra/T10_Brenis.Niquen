def validar_entero(num):
    if (isinstance(num,int)):
        return True
    else:
        return False
#fin def

def validar_rango(num, ri, rf):
    if (validar_entero(num)==True):
        if (num>=ri and num<= rf):
            return True
        else:
            return False
    else:
        return False
#fin def

def pedir_numero(msg,ri,rf):
    n=""
    while(validar_rango(n,ri,rf)==False):
        n=input(msg)
        if (n.isdigit()==True):
            n=int(n)
    return int(n)
#fin def

def pedir_listas(msg):
    archivo=open(msg)
    datos=archivo.readlines()
    lista=[]
    for item in datos:
        lista.append(item.replace("\n",""))
    #fin for
    archivo.close()
    return lista
#fin def
