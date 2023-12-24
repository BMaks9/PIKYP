from pars import print_day
import telebot
bot = telebot.TeleBot("6956846607:AAHRsE-RW-J2w3ChTD0_Agx5Jz4WZizE-1Y")
from telebot import types
name = ' '
@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, "В какой ты группе?")
    bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name

def get_name(message): #получаем фамилию
    global name 
    name = message.text
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key1 = types.InlineKeyboardButton(text='ПН', callback_data='ПН'); #кнопка «Да»
    keyboard.add(key1); #добавляем кнопку в клавиатуру
    key2 = types.InlineKeyboardButton(text='ВТ', callback_data='ВТ')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='СР', callback_data='СР')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='ЧТ', callback_data='ЧТ')
    keyboard.add(key4)
    key5 = types.InlineKeyboardButton(text='ПТ', callback_data='ПТ')
    keyboard.add(key5)
    key6 = types.InlineKeyboardButton(text='СБ', callback_data='СБ')
    keyboard.add(key6)
    bot.send_message(message.from_user.id, text="Выбери день", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.send_message(call.message.chat.id, text= print_day(name, call.data), parse_mode="HTML")
bot.polling(none_stop=True, interval=0)
