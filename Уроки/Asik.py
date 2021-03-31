def factorial(n):
	if n == 1: 
		return 1
	else:
		return factorial(n-1)*n

Chislo = int(input("Введите значение n: "))
print(factorial(Chislo))