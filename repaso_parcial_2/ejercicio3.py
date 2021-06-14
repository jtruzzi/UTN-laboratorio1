import os

def sumar_diccionarios(lista_de_diccs):
    sumatoria_claves = 0
    sumatoria_valores = 0
    for diccionario in lista_de_diccs:
        for key in diccionario.keys():
            sumatoria_claves = sumatoria_claves + key
            sumatoria_valores = sumatoria_valores +  diccionario[key]

    return (sumatoria_claves, sumatoria_valores)

lista_de_diccs=[{1:10, 2:20}, {1:30, 4:40}, {4:50,6:60}]
print(sumar_diccionarios(lista_de_diccs))
