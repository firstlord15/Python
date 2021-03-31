import eel
import pyowm
owm=pyowm.OWM("20f2cbdcf4a9938716387cb7c4606495")


@eel.expose
def get_weather(city):
  mgr=owm.weather_manager()
  observation=mgr.weather_at_place(city)
  w=observation.weather
  temp=w.temperature('celsius')['temp']
  return "В "+ city + " сейчас "+ str(temp) + " ℃"


eel.init('web')
eel.start('main.html')