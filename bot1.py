import telebot
import mainf
import logging
from telebot import types

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(mainf.token_t)

@bot.message_handler(commands=['start'])
def handle_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text='Театр🎭', callback_data='theatre')
    bt_2 = types.InlineKeyboardButton(text='Кино🎬', callback_data='cinema')
    bt_3 = types.InlineKeyboardButton(text='Концерты🎶', callback_data='concert')
    bt_4 = types.InlineKeyboardButton(text='Выставки🖼', callback_data='show')
    bt_5 = types.InlineKeyboardButton(text='Другие события🧐', callback_data='another')
    markup_inline.add(bt_1,bt_2)
    markup_inline.add(bt_3,bt_4)
    markup_inline.add(bt_5)
    start_message = 'Приветствую {},\nМоя цель помочь Вам найти тусу вам на вечер.\n\nВыберите заинтересовавшую вас категорию'.format(message.chat.first_name)
    bot.send_message(message.chat.id, start_message, reply_markup=markup_inline)

@bot.callback_query_handler(lambda a: True)
def start_answer(a):
    if a.data == "concert":
        markup_inline = types.InlineKeyboardMarkup()
        dic = mainf.bulka()
        for i in range(4):
            bt = types.InlineKeyboardButton(list(dic)[i], callback_data=dic.get(list(dic)[i]))
            markup_inline.add(bt)
        bot.send_message(a.message.chat.id, "Рекомендуемые Вам концерты", reply_markup=markup_inline)

    if a.data in list(mainf.concert_data.values()):
        mainf.querydata = a.data
        mainf.chosen_photo(mainf.querydata)
        bot.send_photo(a.message.chat.id, open('img.jpg', 'rb'),mainf.chosen_concert(mainf.querydata))


    if a.data in list(mainf.concert_data.values()) and a.data != mainf.querydata:
        bot.edit_message_media(a.message.chat.id, open('img.jpg', 'rb'))
        bot.edit_message_text(a.message.chat.id, mainf.chosen_concert(mainf.querydata))





bot.polling()
