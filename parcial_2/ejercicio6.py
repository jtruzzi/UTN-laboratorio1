# Variables iniciales
PALOS = [("Corazones", "rojo"), ("Diamantes", "rojo"), ("Picas", "negro"), ("Trebol", "negro")]
NUMEROS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Funciones
def generar_mazo():
    mazo = list()
    for palo, color in PALOS:
        for numero in NUMEROS:
            mazo.append((numero, palo, color))
    return mazo

def ordernar_mazo(mazo):
    return sorted(mazo, key=lambda carta: carta[2])

# Programa
mazo = generar_mazo()
mazo_ordenado = ordernar_mazo(mazo)
for carta in mazo_ordenado:
    print("{} {} de {}".format(carta[0], carta[2], carta[1]))