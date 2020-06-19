import telebot
import random

from telebot import types

bot = telebot.TeleBot('1134044846:AAHAV1GYnv2vdyP6y83XYVD_fqg8hFL8wWs')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open ('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🍺Пиво")
    item2 = types.KeyboardButton("🍷Вино")
    item3 = types.KeyboardButton("Ром")
    item4 = types.KeyboardButton("Коньяк")
    item5 = types.KeyboardButton("Виски")
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы облегчить твой выбор бухлишка на тусу.".format(message.from_user, bot.get_me()),
    parse_mode ='html', reply_markup=markup)

vine = ['Может стоит попробовать красное сухое вино из ЮАР - "BARISTA PINOTAGE"?']

pivo = ['"Essa Lime & Mint"?']

cognaс = ['"Коньяк армянский Старый КС Шалахо 10 лет"']

rum = ['"Captain Morgan"']

whiskey = ['"Grant’s tripple wood"']

choiser = ['Может стоит попробовать - ',
           'Я думаю стоит попробовать - ',
           'Отлично подойдёт - ',
           'Хорошим выбором будет - ',
           'Как насчёт - ',
           'Попробуй - ',
           'Может тебе понравится - ',
           'А как насчёт - ']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.type == 'private':
        if message.text == '🍺Пиво':
            bot.send_message(message.chat.id, str(random.choice(choiser)+random.choice(pivo)))
        elif message.text == '🍷Вино':
            bot.send_message(message.chat.id, str(random.choice(vine)))
        elif message.text == 'Коньяк':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(cognaс)))
        elif message.text == 'Ром':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(rum)))
        elif message.text == 'Виски':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(whiskey)))
        else:
            bot.send_message(message.chat.id, 'Я не знаю что на это ответить 😥')

bot.polling(none_stop=True)