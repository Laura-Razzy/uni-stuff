Algoritmo Potencia
	i <- 0
	x <- 1
	Repetir
		Escribir "Ingrese la base:"
		Leer b
	Hasta Que (b > 0)
	Repetir
		Escribir "Ingrese el exponente:"
		Leer e
	Hasta Que (e >= 0)
	
	Repetir
		x <- (x * b)
		i <- (i + 1)
	Hasta que i = e
	
	Escribir "La base ", b " elevada al exponente ", e " es igual a: ", x
FinAlgoritmo
