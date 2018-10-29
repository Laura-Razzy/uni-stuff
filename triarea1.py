# Dados 3 puntos (x,y) aleatorios haga un programa en python que calcule el area del triangulo

import math
import random

x1 = int(random.random())
x2 = int(random.random())
x3 = int(random.random())
y1 = int(random.random())
y2 = int(random.random())
y3 = int(random.random())

print("a = (%s, %s)" % (x1, y1))
print("b = (%s, %s)" % (x2, y2))
print("c = (%s, %s)" % (x3, y3))

a = math.hypot(x1,y1)
b = math.hypot(x2,y2)
c = math.hypot(x3,y3)
s = 0.5 * (a + b + c)
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(area)
