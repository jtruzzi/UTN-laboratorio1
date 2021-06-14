import os

def sumar_diccionarios(lista1, lista2):
    diccionario = dict()
    for index, item in enumerate(lista1):
        diccionario[item] = lista2[index]
    return diccionario

lista1=["clave1", "clave2", "clave3"]
lista2=["valor1", "valor2", "valor3"]
print(sumar_diccionarios(lista1, lista2))
