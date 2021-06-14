import os

def valores_son_iguales(diccionario):
    iguales = True
    anterior = None
    for value in diccionario.values():
        if value == anterior or anterior == None:
            anterior = value
        else:
            iguales = False
    return iguales

print(valores_son_iguales({"clave1": 1, "clave2": 1, "clave3": 1, "clave4": 1}))
print(valores_son_iguales({"clave1": 2, "clave2": 3, "clave3": 4, "clave4": 1}))
