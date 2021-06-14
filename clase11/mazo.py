import os

palos =  ["basto", "oro", "espadas", "copas"]

def generar_mazo():
    mazo = list()
    for palo in palos:
        for i in range(1,11):
            mazo.append((i, palo))
    return mazo

print(generar_mazo())
