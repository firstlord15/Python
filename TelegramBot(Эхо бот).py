# пишем телеграм бота с помощью модуля pyTelegramBotAPI

import pyowm
import telebot



@bot.message_handler(content_types = ['text'])
def send_echo(message):
        observation = owm.weather_at_place( message.text )
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
        answer += "Температура сейчас ровна " + str(temp) + "\n\n"

        if temp < 10:
            answer += 'Одевайся теплее, сейчас очень холодно' 
        elif temp < 20:
            answer += 'Одевайся по теплее, сейчас холодновато' 
        else:
            answer += 'Температура сейчас теплое, оденся по легче' 

        bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)

