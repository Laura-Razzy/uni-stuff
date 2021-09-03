# Dados 3 puntos (x,y) aleatorios haga un programa en python que calcule el area del triangulo

import math
import random

x1 = random.random()
x2 = random.random()
x3 = random.random()
y1 = random.random()
y2 = random.random()
y3 = random.random()

print("a = (%s, %s)" % (x1, y1))
print("b = (%s, %s)" % (x2, y2))
print("c = (%s, %s)" % (x3, y3))

a = math.hypot(x1,y1)
b = math.hypot(x2,y2)
c = math.hypot(x3,y3)
# s is the semiperimeter of the triangle
s = 0.5 * (a + b + c)
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(area)
