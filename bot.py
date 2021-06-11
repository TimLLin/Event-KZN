from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
import logging
import mainf


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(mainf.token_t, use_context=True)

#########################################
def start(update,context):
    start_message = 'Приветствую {},\nМоя цель помочь Вам найти тусу вам на вечер.\n\nВыберите заинтересовавшую вас категорию'.format(update.message.chat.first_name)
    context.bot.send_message(update.effective_chat.id, start_message, reply_markup=main_menu_keyboard())

#########################################
def main_menu_keyboard():
    markup = [[KeyboardButton(text='Театр🎭'), KeyboardButton(text='Кино🎬')],
              [KeyboardButton(text='Концентры🎶'), KeyboardButton(text='Выставки🖼')],
              [KeyboardButton(text='Другое🧐')]]
    return ReplyKeyboardMarkup(markup, resize_keyboard = True)

#########################################
def main():
    updater.dispatcher.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()