# Funciones
def ordenar_diccionarios(diccionarios):
    return sorted(diccionarios, key=lambda x: len(x.keys()))

# Programa
entrada=[{1:10, 2:20, 3:20}, {1:50}, {1:30, 2:40, 3:40, 4:40}, {1:50, 2:60}]
salida = ordenar_diccionarios(entrada)
print(salida)# [{1:50}, {1:50, 2:60}, {1:10, 2:20, 3:20}, {1:30, 2:40, 3:40, 4:40}]
