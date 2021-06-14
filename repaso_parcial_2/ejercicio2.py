import os

def sumar_diccionarios(lista_de_diccs):
    dicc_combinado = dict()
    for diccionario in lista_de_diccs:
        for key in diccionario.keys():
            if key in dicc_combinado:
                dicc_combinado[key] = dicc_combinado[key] + diccionario[key]
            else:
                dicc_combinado[key] = diccionario[key]

    return dicc_combinado

lista_de_diccs=[{1:10, 2:20}, {1:30, 4:40}, {4:50,6:60}]
print(sumar_diccionarios(lista_de_diccs))
