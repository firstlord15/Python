# второй неизвестный шифратор

letter = "HELLO WORLD"
key = 17
final = ""

for char in letter:
	 if ord(char) in range(65, 91):
	 	final += chr((ord(char)+ key-13)%26 + 65)
	 else:
	 	final += char
print(final)
