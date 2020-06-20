import telebot
import random

from telebot import types

bot = telebot.TeleBot('1134044846:AAHAV1GYnv2vdyP6y83XYVD_fqg8hFL8wWs')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🍺Пиво")
    item2 = types.KeyboardButton("🍷Вино")
    item3 = types.KeyboardButton("Ром")
    item4 = types.KeyboardButton("Коньяк")
    item5 = types.KeyboardButton("Виски")
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы облегчить твой выбор бухлишка на тусу.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


pivo = ['"Essa Lime & Mint"']

p_description1 = 'Вкус: 2/10\nЦена: 45-60\nОпьянение: 8/10\nНе вкусное пиво для девочек.'

vine = ['"BARISTA PINOTAGE"']

v_description1 = 'Вкус: 7/10\nЦена: 700(0.75л)\nОпьянение: 8/10\nМощный, с фруктово–ягодной кислотностью и сладкими джемово–ягодными тонами.'

rum = ['"CAPTAIN MORGAN Original Spiced Gold"']

r_description1 = 'Вкус: 8.3/10\nЦена: 1100(0.7л)\nОпьянение: 8/10\nМягкий,с насыщенным вкусом, хорошо пьется,можно почти не закусывать.'

cognac = ['"Коньяк армянский Старый КС Шалахо 10 лет"']

c_description1 = 'Вкус: 2.5/10\nЦена: 600(0.5л)\nОпьянение: 8.2/10\nТакой себе коньяк, на любителя, цена даже завышена.'

whiskey = ['"Grant’s tripple wood"']

w_description1 = 'Вкус: 7/10\nЦена: 1349(0.7л)\nОпьянение: 8/10\nГлубокий вкус, приятный запах, приемлемая цена.'

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
            global p
            p = random.choice(pivo)
            pivo_markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Описание', callback_data='description')
            pivo_markup.add(item1)
            bot.send_message(message.chat.id, random.choice(choiser) + p, reply_markup=pivo_markup)
            sti1 = open('ESSA lime&mint.webp', 'rb')
            if p == '"Essa Lime & Mint"':
                bot.send_sticker(message.chat.id, sti1)
        elif message.text == '🍷Вино':
            global v
            v = random.choice(vine)
            vine_markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Описание', callback_data='v_description')
            vine_markup.add(item1)
            bot.send_message(message.chat.id, random.choice(choiser) + v, reply_markup=vine_markup)
            sti2 = open('barista_pinotage.webp', 'rb')
            if v == '"BARISTA PINOTAGE"':
                bot.send_sticker(message.chat.id, sti2)
        elif message.text == 'Ром':
            global r
            r = random.choice(rum)
            rum_markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Описание', callback_data='r_description')
            rum_markup.add(item1)
            bot.send_message(message.chat.id, random.choice(choiser) + r, reply_markup=rum_markup)
            sti3 = open('CAPTAIN MORGAN Original Spiced Gold.webp', 'rb')
            if r == '"CAPTAIN MORGAN Original Spiced Gold"':
                bot.send_sticker(message.chat.id, sti3)
        elif message.text == 'Коньяк':
            global c
            c = random.choice(cognac)
            cognac_markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Описание', callback_data='c_description')
            cognac_markup.add(item1)
            bot.send_message(message.chat.id, random.choice(choiser) + c, reply_markup=cognac_markup)
            sti4 = open('shalaho 10years.webp', 'rb')
            if c == '"Коньяк армянский Старый КС Шалахо 10 лет"':
                bot.send_sticker(message.chat.id, sti4)
        elif message.text == 'Виски':
            global w
            w = random.choice(whiskey)
            whiskey_markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton('Описание', callback_data='w_description')
            whiskey_markup.add(item1)
            bot.send_message(message.chat.id, random.choice(choiser) + w, reply_markup=whiskey_markup)
            sti5 = open('Grants-Whisky-Triple-Wood-bottle.webp', 'rb')
            if w == '"Grant’s tripple wood"':
                bot.send_sticker(message.chat.id, sti5)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что на это ответить 😥')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'description':
                if p == '"Essa Lime & Mint"':
                    bot.send_message(call.message.chat.id, p_description1)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=p,
                                          reply_markup=None)
                # elif p == ...
            elif call.data == 'v_description':
                if v == '"BARISTA PINOTAGE"':
                    bot.send_message(call.message.chat.id, v_description1)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=v,
                                          reply_markup=None)
            elif call.data == 'r_description':
                if r == '"CAPTAIN MORGAN Original Spiced Gold"':
                    bot.send_message(call.message.chat.id, r_description1)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=r,
                                          reply_markup=None)
            elif call.data == 'c_description':
                if c == '"Коньяк армянский Старый КС Шалахо 10 лет"':
                    bot.send_message(call.message.chat.id, c_description1)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=c,
                                          reply_markup=None)
            elif call.data == 'w_description':
                if w == '"Grant’s tripple wood"':
                    bot.send_message(call.message.chat.id, w_description1)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text=w,
                                          reply_markup=None)


    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
