import os

diccionario =  dict()
diccionario["clave1"] = "4"
diccionario["clave2"] = "5"
diccionario["clave3"] = "2"
diccionario["clave4"] = "1"
diccionario["clave5"] = "3"

def ordenar_diccionario(diccionario):
    resultado_ordenado = dict()
    for key in sorted(diccionario.keys(), key=lambda key: diccionario[key]):
        resultado_ordenado[key] = diccionario[key]
    return resultado_ordenado

print(ordenar_diccionario(diccionario))
