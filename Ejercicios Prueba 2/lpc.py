#Ejercicio 6 Lana para contar
import random

#Escribe tu codigo para las funciones dado() y cartas()

def dado(f):
    d = int(random.uniform(1,7))
    print("El jugador %s lanza el dado y cae en %s" % (f, d))
    return d

def cartas(f,n):
    for i in range (0,n):
        

def ronda():
    roba_1 = dado(1)
    roba_2 = dado(2)
    cantidad_1 = cartas(roba_1)
    cantidad_2 = cartas(roba_2)
    if (cantidad_1 > cantidad_2):
        print("El jugador 1 gana la ronda!")
        return 1
    if (cantidad_1 < cantidad_2):
        print("El jugador 2 gana la ronda!")
        return 2
    if (cantidad_1 = cantidad_2):
        print("Empate")
        return 0

puntos_1 = 0
puntos_2 = 0

#Escribe tu codigo del programa principal aca

if (puntos_1 == 5):
    print("El ganador es el jugador 1")
if (puntos_2 == 5):
    print("El ganador es el jugador 2")
