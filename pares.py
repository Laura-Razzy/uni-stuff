# haga un programa que sume los numeros pares por un lado y los impares por otro hasta el numero ingresado por el usuario.

def meme(a,b):
    while (a < b):
        a = (a + 2)
    return a

x = input("numero? > ")
par = meme(0,x)
impar = meme(1,x)

print("pares = %s" % par)
print("pares = %s" % impar)
