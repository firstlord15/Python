def printBin(n):
	while n!=0:
		print(n % 2, end = " ")
		n = n // 2

printBin(14)