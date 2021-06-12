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
    start_message = 'Приветствую {},\nМоя цель помочь Вам найти тусу  на вечер.\n\nВыберите заинтересовавшую вас категорию для ознакомления с рекомендациями'.format(message.chat.first_name)
    bot.send_message(message.chat.id, start_message, reply_markup=markup_inline)

@bot.callback_query_handler(lambda a: True)
def start_answer(a):
    if a.data == "concert":
        markup_inline = types.InlineKeyboardMarkup()
        dic = mainf.bulka(mainf.url_data[0])
        mainf.dic1 = mainf.bulka(mainf.url_data[0])
        mainf.url_querry = mainf.url_data[0]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(dic)[i], callback_data=dic.get(list(dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    if a.data == "theatre":
        markup_inline = types.InlineKeyboardMarkup()
        dic = mainf.bulka(mainf.url_data[2])
        print(dic)
        mainf.dic1 = mainf.bulka(mainf.url_data[2])
        mainf.url_querry = mainf.url_data[2]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(dic)[i], callback_data=dic.get(list(dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id,a.message.message_id, reply_markup=markup_inline)

    elif a.data == "show":
        markup_inline = types.InlineKeyboardMarkup()
        dic = mainf.bulka(mainf.url_data[1])
        mainf.dic1 = mainf.bulka(mainf.url_data[1])
        mainf.url_querry = mainf.url_data[1]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(dic)[i], callback_data=dic.get(list(dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id,a.message.message_id, reply_markup=markup_inline)

    elif a.data == "cinema":
        markup_inline = types.InlineKeyboardMarkup()
        dic = mainf.bulka(mainf.url_data[3])
        mainf.dic1 = mainf.bulka(mainf.url_data[3])
        mainf.url_querry = mainf.url_data[3]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(dic)[i], callback_data=dic.get(list(dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id,a.message.message_id, reply_markup=markup_inline)

    elif a.data in list(mainf.dic1.values()):
            try:
                mainf.querydata = a.data
                mainf.chosen_photo(mainf.querydata)
                markup_inline = types.InlineKeyboardMarkup()
                bt_1 = types.InlineKeyboardButton(text='В главное меню', callback_data='back_main_menu_w_edit')
                bt_2 = types.InlineKeyboardButton(text='Назад', callback_data='back_c')
                bt_3 = types.InlineKeyboardButton(text="Купить билет", url = str(mainf.querydata))
                markup_inline.add(bt_3)
                markup_inline.add(bt_2, bt_1)
                bot.send_photo(a.message.chat.id, open('img.jpg', 'rb'), mainf.chosen_concert(mainf.querydata), reply_markup=markup_inline)
            except AttributeError:
                markup_inline = types.InlineKeyboardMarkup()
                bt_1 = types.InlineKeyboardButton(text='В главное меню', callback_data='back_main_menu_w_edit')
                bt_2 = types.InlineKeyboardButton(text='Назад', callback_data='back_c')
                bt_3 = types.InlineKeyboardButton(text="Купить билет", url=str(mainf.querydata))
                markup_inline.add(bt_3)
                markup_inline.add(bt_2, bt_1)
                bot.send_message(a.message.chat.id, mainf.chosen_concert(mainf.querydata),reply_markup=markup_inline)

    elif a.data == 'next':
        mainf.event_index += 5
        markup_inline = types.InlineKeyboardMarkup()
        dic = mainf.bulka(mainf.url_querry)
        for i in range(4):
            if mainf.event_index+i < len(dic):
                bt = types.InlineKeyboardButton(list(dic)[i+mainf.event_index], callback_data=dic.get(list(dic)[i + mainf.event_index]))
                markup_inline.add(bt)
            elif mainf.event_index+i > len(dic):
                markup_inline1 = types.InlineKeyboardMarkup()
                bt_1 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_main_menu")
                markup_inline1.add(bt_1)
                bot.send_message(a.message.chat.id, "Конец списка ремондаций. Если вы не нашли то что искали, перейдите в главное меню и воспользуйтесь рекомендациями в других категориях", reply_markup=markup_inline1 )


        if mainf.event_index + 4 < len(dic):
            bt_b = types.InlineKeyboardButton("➡️", callback_data='next')
            bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
            bt_p = types.InlineKeyboardButton("⬅️", callback_data='previous')
            markup_inline.add(bt_p, bt_menu, bt_b)
        else:
            bt_p = types.InlineKeyboardButton("⬅️", callback_data='previous')
            bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
            markup_inline.add(bt_p, bt_menu)
        bot.edit_message_reply_markup(a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == "previous":
        mainf.event_index -= 5
        markup_inline_back = types.InlineKeyboardMarkup()
        dic = mainf.bulka(mainf.url_querry)
        for i in range(4):
            if mainf.event_index + i > 0:
                bt = types.InlineKeyboardButton(list(dic)[i + mainf.event_index],
                                            callback_data=dic.get(list(dic)[i + mainf.event_index]))
                markup_inline_back.add(bt)
            elif mainf.event_index + i == 0:
                bt = types.InlineKeyboardButton(list(dic)[i + mainf.event_index],
                                                callback_data=dic.get(list(dic)[i + mainf.event_index]))
                markup_inline_back.add(bt)
        if mainf.event_index > 0:
            bt_b = types.InlineKeyboardButton("➡️", callback_data='next')
            bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')

            bt_p = types.InlineKeyboardButton("⬅️", callback_data='previous')
            markup_inline_back.add(bt_p,bt_menu, bt_b)
        else:
            bt_b = types.InlineKeyboardButton("➡️", callback_data='next')
            bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
            markup_inline_back.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id, a.message.message_id, reply_markup=markup_inline_back)

    elif a.data == "back_main_menu":
        markup_inline = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Театр🎭', callback_data='theatre')
        bt_2 = types.InlineKeyboardButton(text='Кино🎬', callback_data='cinema')
        bt_3 = types.InlineKeyboardButton(text='Концерты🎶', callback_data='concert')
        bt_4 = types.InlineKeyboardButton(text='Выставки🖼', callback_data='show')
        bt_5 = types.InlineKeyboardButton(text='Другие события🧐', callback_data='another')
        markup_inline.add(bt_1, bt_2)
        markup_inline.add(bt_3, bt_4)
        markup_inline.add(bt_5)
        bot.edit_message_reply_markup(a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == "back_main_menu_w_edit":
        markup_inline = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Театр🎭', callback_data='theatre')
        bt_2 = types.InlineKeyboardButton(text='Кино🎬', callback_data='cinema')
        bt_3 = types.InlineKeyboardButton(text='Концерты🎶', callback_data='concert')
        bt_4 = types.InlineKeyboardButton(text='Выставки🖼', callback_data='show')
        bt_5 = types.InlineKeyboardButton(text='Другие события🧐', callback_data='another')
        markup_inline.add(bt_1, bt_2)
        markup_inline.add(bt_3, bt_4)
        markup_inline.add(bt_5)
        bot.send_message(a.message.chat.id, "Вы можете ознакомиться с рекомендацими в категориях",
                         reply_markup=markup_inline)

    elif a.data == "back_c":
        bot.delete_message(a.message.chat.id, a.message.message_id)






bot.polling(none_stop=True)