#Программа типо погоды лол с помощью модюла "puown"

from colorama import init
from colorama import Fore, Back, Style

import pyowm


owm = pyowm.OWM('20f2cbdcf4a9938716387cb7c4606495', language = "ru")
init()

print(Fore.BLACK)
print(Back.YELLOW)

place = input ("В каком городе вы живете?")

print(Fore.RED)

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print(Back.CYAN)
print(Fore.BLACK)

print ("В городе " + place + " сейчас " + w.get_detailed_status())
print ("Температура в " + place + " сейчас " + str(temp))

print(Back.WHITE)
print(Fore.BLACK)

if temp < 10:
    print( 'Одевайся теплее, сейчас очень холодно' )
    a = input("Ну как?")
    if a == "Yes":
        print("Ну и ладно")
        
elif temp < 20:
    print( 'Одевайся по теплее, сейчас холодновато' )
else:
    print( 'Температура сейчас теплое, оденся по легче' )

input()

# возможные ошибки : 1) owm = pyowm.OWM('20f2cbdcf4a9938716387cb7c4606495', language = "ru"), language маленькими буквами!
# возможные ошибки : 2) if > 10: НЕ ЗАБЫВАЙ : (else:, if > 10:, elif > 20:)
 

