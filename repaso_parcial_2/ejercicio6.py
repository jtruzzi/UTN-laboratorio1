import os

def valores_mas_altos(diccionario):
    claves = sorted(diccionario.keys(), key=lambda x: diccionario[x], reverse= True)[:3]
    valores = []
    for clave in claves:
        valores.append(diccionario[clave])
    return valores

diccionario={"clave1": 9, "clave2": 7, "clave3": 2, "clave4": 4, "clave5": 10}
print(valores_mas_altos(diccionario))
