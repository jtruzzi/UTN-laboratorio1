import os

def valores_unicos(diccionario):
    valores_unicos = list()
    for value in diccionario.values():
        if not value in valores_unicos: 
            valores_unicos.append(value) 
    return valores_unicos

diccionario={"clave1": "Valor1", "clave2": "Valor1", "clave3": "Valor1", "clave4": "Valor2"}
print(valores_unicos(diccionario))
