a = 0
b = 1
aux = ""

sequenciaFibonacci = list() 

for i in range(10):
    aux = a
    a = a + b
    b = aux
    sequenciaFibonacci.append(aux) 

valor = int(input("Digite um valor: "))

print(sequenciaFibonacci)

if valor in sequenciaFibonacci :
	print("O número pertence a sequência de Fibonacci ")
else:
    print("O número não pertence a sequência de Fibonacci ")