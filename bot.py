from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import logging
import mainf


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(mainf.token_t, use_context=True)

SELECTING_LEVEL, CONCERT_LEVEL = map(chr,range(2))
END = ConversationHandler.END
#########################################
def start(update,context):
    start_message = 'Приветствую {},\nМоя цель помочь Вам найти тусу вам на вечер.\n\nВыберите заинтересовавшую вас категорию'.format(update.message.chat.first_name)
    context.bot.send_message(update.effective_chat.id, start_message, reply_markup=main_menu_keyboard())
    return SELECTING_LEVEL

def concert_recomendation(update,context):
    context.bot.send_message(update.effective_chat.id,"Рекомендуемые Вам концерты", reply_markup=concert_recomendation_keyboard())
    return CONCERT_LEVEL

def concert_info(update,context):
    message = mainf.chosen_concert()
    context.bot.send_message(update.effective_chat.id, message[2])

def stop(update, context):
    context.bot.send_message(update.effective_chat.id, "Ну и пошел ты")
    return END
#########################################
def main_menu_keyboard():
    markup = [[KeyboardButton(text='Театр🎭'), KeyboardButton(text='Кино🎬')],
              [KeyboardButton(text='Концентры🎶'), KeyboardButton(text='Выставки🖼')],
              [KeyboardButton(text='Другое🧐')]]
    return ReplyKeyboardMarkup(markup, resize_keyboard=True)

def concert_recomendation_keyboard():
    i = 0
    dic = mainf.bulka()
    keyboard = [[InlineKeyboardButton(list(dic)[i], callback_data=dic.get(list(dic)[i])), InlineKeyboardButton(list(dic)[i+1], callback_data=dic.get(list(dic)[i+1]))],
                [InlineKeyboardButton(list(dic)[i+2], callback_data=dic.get(list(dic)[i + 3])), InlineKeyboardButton(list(dic)[i + 3], callback_data=dic.get(list(dic)[i + 3]))],
                [InlineKeyboardButton(list(dic)[i + 4], callback_data=dic.get(list(dic)[i + 4]))],
                [InlineKeyboardButton('Дальше', callback_data='next')]]

    return InlineKeyboardMarkup(keyboard)

#def concert_recommedation_edit_keyboard()

#########################################
def main():
    updater.dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECTING_LEVEL: [MessageHandler(Filters.regex('Концентры🎶'), concert_recomendation)],
            CONCERT_LEVEL : [CallbackQueryHandler(concert_info,pattern="/concert/2049288/")]

        },
        fallbacks=[CommandHandler('start', start)]
    ))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()