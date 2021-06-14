import os

palos =  ["basto", "oro", "espadas", "copas"]

def obtener_peso(numero, palo):
    print(numero, palo)
    if numero == 1 and palo == 'espadas':
        return 19
    elif numero == 1 and palo == 'basto':
        return 18
    elif numero == 7 and palo == 'espadas':
        return 17
    elif numero == 7 and palo == 'oro':
        return 16
    elif numero == 3:
        return 15
    elif numero == 2:
        return 14
    elif numero == 1:
        return 13
    else:
        return numero

def generar_mazo():
    mazo = list()
    for palo in palos:
        for numero in range(0,12):
            if numero != 8 and numero != 9:
                peso = obtener_peso(numero + 1, palo)
                mazo.append((numero + 1, palo, peso))
    return mazo

def ordenar_mazo(mazo):
    return sorted(mazo, key=lambda carta: carta[2], reverse=True)

mazo = generar_mazo()
print(ordenar_mazo(mazo))
