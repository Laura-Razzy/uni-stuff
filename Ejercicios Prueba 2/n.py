def yeet(a,b):
    return (a ** b)

n = int(input("Ingrese un numero: "))
m = int(input("Ingrese una cantidad de veces: "))
a = n

for i in range(2,m+1):
    a = a + yeet(n,i)

print(a)
