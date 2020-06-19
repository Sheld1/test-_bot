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

pivo = ['"Essa Lime & Mint"']

sti1 = open ('ESSA lime&mint.webp', 'rb')

vine = ['Может стоит попробовать красное сухое вино из ЮАР - "BARISTA PINOTAGE"?']

sti2 = open ('barista_pinotage.webp', 'rb')

rum = ['"CAPTAIN MORGAN Original Spiced Gold"']

sti3 = open ('CAPTAIN MORGAN Original Spiced Gold.webp', 'rb')

cognaс = ['"Коньяк армянский Старый КС Шалахо 10 лет"']

sti4 = open ('shalaho 10years.webp', 'rb')

whiskey = ['"Grant’s tripple wood"']

sti5 = open ('Grants-Whisky-Triple-Wood-bottle.webp', 'rb')

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
            if message.text == 'Essa Lime & Mint':
                bot.send_sticker(message.chat.id, sti1)
        elif message.text == '🍷Вино':
            bot.send_message(message.chat.id, str(random.choice(vine)))
            if message.text == 'Essa Lime & Mint':
                bot.send_sticker(message.chat.id, sti2)
        elif message.text == 'Ром':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(rum)))
            if message.text == 'Essa Lime & Mint':
                bot.send_sticker(message.chat.id, sti3)
        elif message.text == 'Коньяк':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(cognaс)))
            if message.text == 'Essa Lime & Mint':
                bot.send_sticker(message.chat.id, sti4)
        elif message.text == 'Виски':
            bot.send_message(message.chat.id, str(random.choice(choiser) + random.choice(whiskey)))
            if message.text == 'Essa Lime & Mint':
                bot.send_sticker(message.chat.id, sti5)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что на это ответить 😥')

bot.polling(none_stop=True)
