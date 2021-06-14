import os

lista_tuplas =  [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

def eliminar_vacias(lista_tuplas):
    elementos = list()
    for tupla in lista_tuplas:
        if tupla:
            elementos.append(tupla)
    return elementos

print(eliminar_vacias(lista_tuplas))
