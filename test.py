import libreria

assert(libreria.validar_entero("hola")==False)
assert(libreria.validar_entero(354.37)==False)
assert(libreria.validar_entero(False)==True)
assert(libreria.validar_entero(13)==True)
print("validar entero -> ok")

assert(libreria.validar_rango(15, 0, 7)==False)
assert(libreria.validar_rango(30, 10, 50)==True)
print("validar rango -> ok")
