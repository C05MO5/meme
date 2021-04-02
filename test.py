#int
#est = 5
#float
#n = 5.7
#str
#nm = "gebv"
#bool
#tatus = True
#

#перервод строки
#print('asfa\nsaf')

#контектация
#print("afa " + str(nm) + " asdas")


#name = input("your name: ")
#age = input("age??: ")
#
#print(name + " s old " + age)

# + .- . *. / .**. %
#
#a = 5
#b = 54
#
#c = a + b
#
#print(c)
#


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<
#calculator
#from colorama import Fore, Back, Style
#from colorama import init
#
#init()
#
#print(Fore.BLACK)
#print(Back.GREEN)
#
#a = input("+ or -: ")
#print(Back.RED)
#b = float( input(" first number: ") )
#print(Back.YELLOW)
#c = float( input(" second number: ") )
#
#if a == "+":
#    d = b + c
#elif a == "-":
#    d = b + c
#
#print(d)
#
#input()

#WEATHER APP

#import pyowm
#language = "ru"
#
#owm = pyowm.OWM('ba4b56a068f488927f48f1860b7900f8')
#mgr = owm.weather_manager()
#
#place = input("city: ")
#
#observation = mgr.weather_at_place(place)
#w = observation.weather
#
#print("В городе " + str(place) + " сейчас " + w.detailed_status + "!!")

#import pyowm
#import telebot
#
#owm = pyowm.OWM('ba4b56a068f488927f48f1860b7900f8')
#mgr = owm.weather_manager()
#bot = telebot.TeleBot("1619383425:AAFbKaYadFRAu7rHsoVNTZ8XOh6sv-OSSPU")
#
#@bot.message_handler(content_types=['text'])
#def send_welcome(message):
##	bot.reply_to(message, message.text)
#    observation = mgr.weather_at_place(message.text)
#    w = observation.weather
#
#    answer = "In city " + str(message.text) + " now " + w.detailed_status + "!!" 
#
#    bot.send_message(message.chat.id, answer)
#bot.polling(none_stop = True)

print("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┗━┻━┻━┻┛┗━━━┛")
