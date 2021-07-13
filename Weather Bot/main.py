import telebot
from pyowm import OWM
import config

owm = OWM(config.owm_token)
bot = telebot.TeleBot(config.bot_token)

def weather(mfu):
    place = mfu
    print(place)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    t = w.temperature('celsius')
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']
    return f'В городе {place} температура: {round(t1, 1)}°, ощущается как {round(t2, 1)}°.\nМаксимальная и минимальная температуры: {round(t3, 1)}°, {round(t4, 1)}°.'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет! Я могу узнать погоду в любом городе мира, отправь мне /help.')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Просто напиши название города :)')
    elif message.text != '/help' and message.text != '/start':
        mfu = message.text
        try:
            bot.send_message(message.from_user.id, weather(mfu))
        except: bot.send_message(message.from_user.id, 'Похоже что это не название города')

bot.polling(none_stop=True, interval=0)

#mgr = owm.weather_manager()
#observation = mgr.weather_at_place(place)
#w = observation.weather
#t = w.temperature('celsius')
#t1 = t['temp']
#t2 = t['feels_like']
#t3 = t['temp_max']
#t4 = t['temp_min']
#print(f'В городе {place} температура {t1}, ощущается как {t2}, максимальная {t3}, минимальная {t4}')
