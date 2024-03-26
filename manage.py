import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '6750835343:AAG8AbiQphxwT7L-EIea3l4Dcfo9C1GQZe4'
bot = telebot.TeleBot(TOKEN)

def start(update, context):
    keyboard = [[InlineKeyboardButton("Watch Video", callback_data='watch_video')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Press the button to watch the video:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    if query.data == 'watch_video':
        query.message.reply_video(video='http://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_30mb.mp4')

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
