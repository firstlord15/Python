# Закидываем это в список)

test = []

lol = input("1: ")
lol2 = input("2: ")
lol3 = input("3: ")
lol4 = input("4: ")
lol5 = input("5: ")
lol6 = input("6: ")

test.append(lol) #Добавить что угодно, но только в конец
test.append(lol2)#Добавить что угодно, но только в конец
test.append(lol3)#Добавить что угодно, но только в конец
test.append(lol4)#Добавить что угодно, но только в конец
test.append(lol5)#Добавить что угодно, но только в конец
test.append(lol6)#Добавить что угодно, но только в конец

print( 'В массиве у нас находится ' + str(len(test)) + ' элементов')
print(test)

delete = input('Что вы хотите удалить?: ')
test.remove(delete)#удалит что угодно

print(test)
print( 'В массиве у нас находится ' + str(len(test)) + ' элементов')

dobavit = input("Что добавить: ")
test.insert(1, dobavit) #Добавть куда хочешь

print(test)
print( 'В массиве у нас находится ' + str(len(test)) + ' элементов')

print ( 'Самое больщое число: ' + max(test) )#выведиться самое большое число

print ( 'Самое маленькое число: ' + min(test) )#выведиться самое маленькое число

co = input ('какое чило сколько повторяется: ')
print(test.count(co)) #какое чило сколько повторяется
             
print(test.reverse)# пишет все значения в обратном порядке
