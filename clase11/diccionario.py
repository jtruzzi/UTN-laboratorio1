import os

noticias = [
    "El futbolista fue atendido en el terreno terreno terreno terreno terreno terreno terreno terreno terreno terreno de juego y evacuado por los servicios de emergencias 15 minutos después de su caída. Acto seguido, la UEFA anunció que el partido había sido postergado con un breve comunicado. ”El partido de la UEFA EURO 2020 en Copenhague ha sido suspendido debido a una emergencia médica”, indicó el máximo organismo del fútbol europeo. Tras eso, y con la tranquilidad en cuanto a la salud del futbolista, el ente informó que el compromiso se reanudaría a las 20.30 hora local (15.30 en la Argentina).",
    "También ayer a la tarde, de manera oficial, la Dra. Claudia Volonte, directora del Cantegril, sostuvo que Susana se encontraba bien e internada en una sala común. “Ingresó estable con todos los parámetros normales hemodinámicos. Presentó una leve insuficiencia respiratoria y sin otros signos generales o de patología Covid, pero era necesario hacer otros controles más estrictos y por eso se determinó su internación. No está con respiración asistida, sino con oxígeno y se moviliza por sus propios medios”, precisó la especialista.",
    "A raíz de lo sucedido, la Justicia local abrió una investigación para determinar si se trató de un caso de gatillo fácil. Como parte de la misma se detuvo de cinco efectivos de la fuerza, en función de lo dispuesto por la Fiscalía de Derechos Humanos de Sáenz Peña. Más tarde, el gobernador Capitanich confirmó los arrestos en las redes sociales y condenó la violencia policial."
]

def obtener_no_permitidas():
    dirname = os.path.dirname(__file__)
    no_permitidas = []
    for linea in open(os.path.join(dirname, 'palabras.txt'), encoding='utf-8'):
        no_permitidas.append(linea.split(".")[1].strip().lower())
    return no_permitidas

def calcular_palabras(noticia):
    no_permitidas = obtener_no_permitidas()
    palabras = dict()
    for palabra in noticia.split(" "):
        if palabra.lower() not in no_permitidas:
            if not palabra in palabras:
                palabras[palabra] = 1
            else:
                palabras[palabra] = palabras[palabra] + 1
    return palabras

def palabra_mas_usada(palabras):
    apariciones = 0
    palabraMasUsada = None
    for palabra, cantidad in palabras.items():
        if cantidad > apariciones:
            palabraMasUsada = palabra
            apariciones = cantidad
    return palabraMasUsada

for i in range(0,3):
    print("")
    print("La noticia:")
    print(noticias[i])
    print("")
    palabras = calcular_palabras(noticias[i])
    print("Contiene las siguientes palabras:")
    print(palabras)
    print("La palabra mas repetida es:", palabra_mas_usada(palabras))
