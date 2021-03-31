#Программа типо погоды лол с помощью модюла "puown"
import pyowm


owm = pyowm.OWM('20f2cbdcf4a9938716387cb7c4606495')
ngr = owm.weather_manager()

place = input ("В каком городе вы живете?: ")


observation = ngr.weather_at_place(place)
w = observation.weather

temp = w.get_temperature('celsius')["temp"]
time = w.get_reference_time(timeformat = 'iso')
clouds = w.get_clouds()



print ("В городе " + place + " сейчас " + w.get_detailed_status())
print ("Температура: " + "примерно " + str(temp) + " градуса по Цельсию")
print ('Время и дата в '+ place + ' сейчас ' + str(time))
print ("Облока: " + str(clouds))

if temp < 5:
    print( 'Одевайся теплее, сейчас очень холодн,' )
    print("при холодной погоде стоит пить горячий кофе.")
elif temp < 10:
    print( 'Одевайся по теплее, сейчас холодновато' )
    print("поэтому стоит еще и посидеть дома и смотреть фильм")
else:
    print( 'Температура сейчас теплое, оденся по легче' )
    print(" поиграй на улице или погуляй с друзьями. ")

input()

# возможные ошибки : 1) owm = pyowm.OWM('20f2cbdcf4a9938716387cb7c4606495', language = "ru"), language маленькими буквами!
# возможные ошибки : 2) if > 10: НЕ ЗАБЫВАЙ : (else:, if > 10, elif > 20:)
 

#city = input('Введите город: ')

#owm = pyowm.OWM('20f2cbdcf4a9938716387cb7c4606495')
#ngr = owm.weather_manager()

#observation = ngr.weather_at_place(city)
#w = observation.weather

#temp = w.temperature("celsius")["temp"]

#print('В городе '+ city + ' сйчас ' + str(temp) + ' градусов!')


