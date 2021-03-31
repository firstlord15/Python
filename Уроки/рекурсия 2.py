def funo_step(a, b):
	if b == 0:
		return 1
	else:
		return a * funo_step(a, b-1)
print(funo_step(2, 4))