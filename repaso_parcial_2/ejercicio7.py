def valores_son_iguales(diccionario):
    valores = list(diccionario.values())
    elemento = valores[0]
    iguales = True
    
    for valor in valores:
        if valor != elemento:
            iguales = False
        else:
            elemento = valor
    return iguales

print(valores_son_iguales({"clave1": 1, "clave2": 1, "clave3": 1, "clave4": 1}))
print(valores_son_iguales({"clave1": 2, "clave2": 3, "clave3": 4, "clave4": 1}))
