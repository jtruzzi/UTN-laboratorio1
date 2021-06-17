diccionario={4:10, 5:40, 20:60, 50:110}
tuplas = list()
for clave, valor in diccionario.items():
    divisible = valor % clave == 0)
    tuplas.append((clave, divisible))

print(tuplas)
