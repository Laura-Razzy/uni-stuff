n = input("Numero? ")
e = input("Exponente? ")
i = 0
a = 1

while True:
    a = (a * n)
    i = (i + 1)
    if i == e: break

print("El numero seria %r" % a)
