#v2
from colorama import init
from colorama import Fore, Back, Style

init()

print (Fore.BLACK)
print (Back.GREEN )

what = input ( "Что делаем? (+, -) " )

print (Back.CYAN )

a = float (input ("введи первое число "))
b = float (input ("введи второе число "))

print (Back.YELLOW )

if what == "+":
    c = a + b
elif what == "-":
    c = a - b
else:
    print("Результат: не выбрано операция" )

print("Результат: " + str( c ))

input()

#возможные ошибки: 1)то что преред input ("введи первое число ") не стои float or int
#возможные ошибки: 2) то что мы ("Результат: " + c ) нет srt(c)
#возможные ошибки: 3) print (Fore.BLACK), если BLACK написан не большими буквами, это важно!

