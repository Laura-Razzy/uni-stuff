Algoritmo Ejemplo
	Escribir "Ingresar horas trabajadas"
	Leer Horas
	Escribir "Ingresar valor hora"
	Leer Valor_hora
	Si Horas<= 44 Entonces
		TOTAL <- Valor_hora*Horas
	SiNo
		TOTAL <- (Horas-44)*1.5*Valor_hora+(44*Valor_hora)
	FinSi
	Escribir "Su sueldo es: ",TOTAL
FinAlgoritmo
