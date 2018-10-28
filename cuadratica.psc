Algoritmo Cuadratica
	Escribir "a?"
	Leer a
	Escribir  "b?"
	leer b
	Escribir "c?"
	leer c
	
	d <- b ^ 2 - 4 * a * c
	v <- -1 * (b / 2 * a)
	
	Si b < 0
		Escribir "Ambas respuesas son imaginarias"
	SiNo
		Si d = 0
			x <- (b + rc(d)) / (2 * a)
			Escribir "Ambas respuestas son: ", x
		SiNo
			x1 <- (b + rc(d)) / (2 * a)
			x2 <- (b - rc(d)) / (2 * a)
			Escribir "Las respuestas son: x1= ", x1 "x2 = ", x2
		FinSi
		Escribir "El vertice es: ", v
	FinSi
FinAlgoritmo
