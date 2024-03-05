a = 0
b = 1
sequenciaFibonacci = list() 

valor = int(input("Digite um valor: "))

while a <= valor :
    aux = a
    a = a + b
    b = aux
    sequenciaFibonacci.append(aux) 
print("Lista de Fibonacci:",sequenciaFibonacci)

if valor in sequenciaFibonacci :
	print("O número pertence a sequência de Fibonacci ")
else:
    print("O número não pertence a sequência de Fibonacci ")