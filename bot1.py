import telebot
import mainf
import logging
import random
import nltk
from telebot import types

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(mainf.token_a)

@bot.message_handler(commands=['start'])
def handle_command(message):
    markup_inline = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton(text='Театр🎭', callback_data='theatre')
    bt_2 = types.InlineKeyboardButton(text='Кино🎬', callback_data='cinema')
    bt_3 = types.InlineKeyboardButton(text='Концерты🎶', callback_data='concert')
    bt_4 = types.InlineKeyboardButton(text='Выставки🖼', callback_data='show')
    bt_5 = types.InlineKeyboardButton(text='Случайное меропритие🔮', callback_data='another')
    markup_inline.add(bt_1,bt_2)
    markup_inline.add(bt_3,bt_4)
    markup_inline.add(bt_5)
    start_message = 'Приветствую {},\nМоя цель помочь Вам найти тусу  на вечер.\n\nВыберите заинтересовавшую вас категорию для ознакомления с рекомендациями.'.format(message.chat.first_name)
    bot.send_message(message.chat.id, start_message, reply_markup=markup_inline)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "*Как пользоваться Ботом?*\nИспользуй кнопки для навигации по рекомендациям или ищите необходимое Вам мероприятие\n\n/start - команда, запускающая бота\n/help - краткая справка\n/search - режим поиска,введите название искомого события и Бот отправит Вам карточку мероприятия.", parse_mode="Markdown")

@bot.message_handler(commands=['search'])
def search_message(message):
    sent = bot.send_message(message.chat.id, "Введите название исполнителя или меропрития и Бот отправит необходимую информацию.")
    bot.register_next_step_handler(sent, search_event)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'старт' or message.text.lower() == 'привет' or message.text.lower() == "start":
        return handle_command(message)

def search_event(message):
    user_data = message.text.lower()
    check_answer = 0
    markup_inline = types.InlineKeyboardMarkup()
    for i in range(4):
        mainf.dic = mainf.bulka(mainf.url_data[i])
        for elem in list(mainf.dic):
            dist = nltk.edit_distance(user_data,elem.lower())
            if dist/len(user_data) <= 0.4:
                bt_1 = types.InlineKeyboardButton(elem, callback_data=mainf.dic.get(elem))
                markup_inline.add(bt_1)
                bot.send_message(message.chat.id,"Нажмите на кнопку для получения информации о мероприятии", reply_markup=markup_inline)
                check_answer += 1
                break
    if check_answer == 0:
        bot.send_message(message.chat.id, "Данного меропрития не существует, проверьте правильность написания и используйте команду /search ещё раз.")




@bot.callback_query_handler(lambda a: True)
def start_answer(a):
    if a.data == "concert":
        markup_inline = types.InlineKeyboardMarkup()
        mainf.dic = mainf.bulka(mainf.url_data[0])
        mainf.url_querry = mainf.url_data[0]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(mainf.dic)[i], callback_data=mainf.dic.get(list(mainf.dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == "theatre":
        markup_inline = types.InlineKeyboardMarkup()
        mainf.dic = mainf.bulka(mainf.url_data[2])
        mainf.url_querry = mainf.url_data[2]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(mainf.dic)[i], callback_data=mainf.dic.get(list(mainf.dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id,a.message.message_id, reply_markup=markup_inline)

    elif a.data == "show":
        markup_inline = types.InlineKeyboardMarkup()
        mainf.dic = mainf.bulka(mainf.url_data[1])
        mainf.url_querry = mainf.url_data[1]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(mainf.dic)[i], callback_data=mainf.dic.get(list(mainf.dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id,a.message.message_id, reply_markup=markup_inline)

    elif a.data == "cinema":
        markup_inline = types.InlineKeyboardMarkup()
        mainf.dic = mainf.bulka(mainf.url_data[3])
        mainf.url_querry = mainf.url_data[3]
        for i in range(4):
            bt = types.InlineKeyboardButton(list(mainf.dic)[i], callback_data=mainf.dic.get(list(mainf.dic)[i]))
            markup_inline.add(bt)
        bt_b = types.InlineKeyboardButton('➡️', callback_data='next')
        bt_menu = types.InlineKeyboardButton('👉🏻🏠👈🏻', callback_data='back_main_menu')
        markup_inline.add(bt_menu, bt_b)
        bot.edit_message_reply_markup(a.message.chat.id,a.message.message_id, reply_markup=markup_inline)

    elif a.data in list(mainf.dic.values()):
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
        #mainf.dic = mainf.bulka(mainf.url_querry)
        for i in range(4):
            if mainf.event_index+i < len(mainf.dic):
                bt = types.InlineKeyboardButton(list(mainf.dic)[i+mainf.event_index], callback_data=mainf.dic.get(list(mainf.dic)[i + mainf.event_index]))
                markup_inline.add(bt)
            elif mainf.event_index+i > len(mainf.dic):
                markup_inline1 = types.InlineKeyboardMarkup()
                bt_1 = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_main_menu")
                markup_inline1.add(bt_1)
                bot.send_message(a.message.chat.id, "Конец списка ремондаций. Если вы не нашли то что искали, перейдите в главное меню и воспользуйтесь рекомендациями в других категориях", reply_markup=markup_inline1 )


        if mainf.event_index + 4 < len(mainf.dic):
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
        #dic = mainf.bulka(mainf.url_querry)
        for i in range(4):
            if mainf.event_index + i > 0:
                bt = types.InlineKeyboardButton(list(mainf.dic)[i + mainf.event_index],
                                            callback_data=mainf.dic.get(list(mainf.dic)[i + mainf.event_index]))
                markup_inline_back.add(bt)
            elif mainf.event_index + i == 0:
                bt = types.InlineKeyboardButton(list(mainf.dic)[i + mainf.event_index],
                                                callback_data=mainf.dic.get(list(mainf.dic)[i + mainf.event_index]))
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
        bt_5 = types.InlineKeyboardButton(text='Случайное меропритие🔮', callback_data='another')
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
        bt_5 = types.InlineKeyboardButton(text='Случайное меропритие🔮', callback_data='another')
        markup_inline.add(bt_1, bt_2)
        markup_inline.add(bt_3, bt_4)
        markup_inline.add(bt_5)
        bot.send_message(a.message.chat.id, "Вы можете ознакомиться с рекомендацими в категориях",
                         reply_markup=markup_inline)

    elif a.data == "back_c":
        bot.delete_message(a.message.chat.id, a.message.message_id)

    elif a.data == "another":
        markup_inline = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Овен♈', callback_data='quest1')
        bt_2 = types.InlineKeyboardButton(text='Телец♉', callback_data='quest1')
        bt_3 = types.InlineKeyboardButton(text='Близнецы♊', callback_data='quest1')
        bt_4 = types.InlineKeyboardButton(text='Рак♋', callback_data='quest1')
        bt_5 = types.InlineKeyboardButton(text='Лев♌', callback_data='quest1')
        bt_6 = types.InlineKeyboardButton(text='Дева♍', callback_data='quest1')
        bt_7 = types.InlineKeyboardButton(text='Весы♎', callback_data='quest1')
        bt_8 = types.InlineKeyboardButton(text='Скорпион♏', callback_data='quest1')
        bt_9 = types.InlineKeyboardButton(text='Стрелец♐', callback_data='quest1')
        bt_10 = types.InlineKeyboardButton(text='Козерог♑', callback_data='quest1')
        bt_11 = types.InlineKeyboardButton(text='Водолей♒', callback_data='quest1')
        bt_12 = types.InlineKeyboardButton(text='Рыбы♓', callback_data='quest1')
        bt_13 = types.InlineKeyboardButton(text='👉🏻🏠👈🏻', callback_data='back_main_menu_w_edit')
        markup_inline.add(bt_1, bt_2, bt_3, bt_4, bt_5, bt_6, bt_7, bt_8, bt_9, bt_10, bt_11, bt_12, bt_13)
        bot.edit_message_text("Бот подберет вам случайное меропритие. Но сперва необходимо ответить на несколько вопросов.\n\n1. Кто Вы по знаку зодиака?", a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == 'quest1':
        markup_inline = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='Да', callback_data='quest2_yes')
        bt_2 = types.InlineKeyboardButton(text='Нет', callback_data='quest2_no')
        bt_3 = types.InlineKeyboardButton(text='👉🏻🏠👈🏻', callback_data='back_main_menu_w_edit')
        markup_inline.add(bt_1, bt_2)
        markup_inline.add(bt_3)
        bot.edit_message_text("Прекрасно-прекрасно, перейдем к следующему вопросу.\n\n2. Вы страдаете от неразделенной любви?", a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == 'quest2_yes' or a.data == 'quest2_no':
        choosen = a.data
        markup_inline = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='ДАА🤫', callback_data='quest3')
        bt_2 = types.InlineKeyboardButton(text='НЕЕТ😠', callback_data='quest3')
        bt_3 = types.InlineKeyboardButton(text='Что это?🧐', callback_data='quest3')
        bt_4 = types.InlineKeyboardButton(text='👉🏻🏠👈🏻', callback_data='back_main_menu_w_edit')
        markup_inline.add(bt_1, bt_2)
        markup_inline.add(bt_3)
        markup_inline.add(bt_4)

        if choosen == 'quest2_yes':
            bot.edit_message_text("Ох забей на него, люди временны, а Бот навсегда. Однако нужно ответить на последний вопрос.\n\n3. Вы верите в теорию квантового бессметрия?\n\nНерабочая версия", a.message.chat.id, a.message.message_id, reply_markup=markup_inline)
        elif choosen == 'quest2_no':
            bot.edit_message_text("Бот искренне рад за тебя. Осталось ответить на последний вопрос.\n\n3. Вы верите в теорию квантового бессметрия?\n\nНерабочая версия", a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == 'quest3':
        markup_inline = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton(text='🎉Получить рекомендацию🎉', callback_data='another_recomendation')
        markup_inline.add(bt_1)
        bot.edit_message_text("Ура Бот получил всю необходимую информацию, сейчас Вы получите меропритие лично для Вас.", a.message.chat.id, a.message.message_id, reply_markup=markup_inline)

    elif a.data == "another_recomendation":
        if len(mainf.dic) != 0:
            index = random.randint(0, len(mainf.dic)-1)
            a.data = mainf.dic.get(list(mainf.dic)[index])
            start_answer(a)
        else:
            i = random.randint(0, 3)
            mainf.dic = mainf.bulka(mainf.url_data[i])
            index = random.randint(0, len(mainf.dic)-1)
            a.data = mainf.dic.get(list(mainf.dic)[index])
            start_answer(a)



bot.polling(none_stop=True)