#Ejercicio 1 Adivina el numero
import random

x = int(random.uniform(1,11))
i = 0

while ((a != x) and (i < 3)):
    a = int(input("Adivina que numeroe ntre 1 y 10 he seleccionado > "))\
    if (x > a):
        print("Fallaste. Mi numero es mayor que %s" % a)
    if (x < a):
        print("Fallaste. Mi numero es menor que %s" % a)
    if (x != a):
        i = (i + 1)

if (a = x):
    print("Correcto! Has adivinado!")
if (i = 3):
    print("Perdiste. Era el %s. Gastate tus tres intentos.")
