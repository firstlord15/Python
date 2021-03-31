def print_bin(n):
	if n == 0: 
		return 0
	print_bin( n // 2)
	print( n % 2, end="")

print_bin(14)