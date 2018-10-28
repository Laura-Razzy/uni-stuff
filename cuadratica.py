import math

a = float(input("a? >"))
b = float(input("b? >"))
c = float(input("c? >"))

d = ((b**2)-(4*a*c)) #discriminante
v = (-1*(b/(2*a))) #vertice
if (v==-0.0): #porque a=1, b=0 y c=0 daba v=-0.0
    v = 0.0

if (d<0):
    print("Ambas respuestas son imaginarias.")
else:
    x1 = ((b+math.sqrt(d))/(2*a))
    x2 = ((b-math.sqrt(d))/(2*a))
    if (x1==x2):
        print("Solo hay una respuesta: %r" % x1)
    else:
        print("Las respuestas son %r y %r" % (x1, x2))
print("El vertice es %r" % v)
