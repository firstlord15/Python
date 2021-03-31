# Программа для копирования файлов! v.1.0.3
print('[Programm Start]')

filename1 = input('Введите название файла забэкапить: ')
filename2 = 'backup ' + filename1

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')

file2.write ( file1.read() )

file1.close()
file2.close()

print('[Programm Stoped]')