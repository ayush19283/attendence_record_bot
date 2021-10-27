from telegram.ext import Updater, CommandHandler, MessageHandler,InlineQueryHandler, Filters,CallbackContext
from telegram import Update, Bot
from datetime import date
import os

TOKEN = os.environ.get('token')
mybot = Bot(TOKEN)
d=date.today()
d=str(d)
def ab(update, context):
    print(update.message.chat.id)
    update.message.reply_text("hello")
     
    print(update.message.text)
def date(update,context):
    print(update.message.chat.id)
    update.message.reply_text(d)
    print(dir(update.message))
    print(update.message.from_user.id)
updater = Updater(TOKEN , use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("hi", ab))
dp.add_handler(CommandHandler("date",date))
#dp.add_handler(MessageHandler(Filters.text&(~Filters.command), hi))
updater.start_polling()
updater.idle()
