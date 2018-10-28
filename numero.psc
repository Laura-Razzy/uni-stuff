Algoritmo A7
	Escribir "Entre un nnumero de [1-100]"
	x <- 50
	t <- 50
	r <- "No Se"

	Mientras r != "igual"
		Escribir "Es mayor, menor o igual que ", x
		t <- t/2
		Leer r
		Si r = "mayor"
			x <- trunc[x + t]
		FinSi		
		Si r = "menor"
			x <- trunc[x - t]
		FinSi
	FinMientras
	
	Escribir "El numero es ", x
FinAlgoritmo
