import pyttsx3

words = input('Введите то что скажит пк: ')
engine = pyttsx3.init()
engine.say(words)
engine.runAndWait()

