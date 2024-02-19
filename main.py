import telebot
from telegram import Update
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '6750835343:AAG8AbiQphxwT7L-EIea3l4Dcfo9C1GQZe4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    greeting_text = f"Hello, {user_name}! 👋\n\nPlease share your contact"

    # Create a custom keyboard with a "Share Contact" button
    keyboard = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True, is_persistent=True)
    button1 = KeyboardButton(text="Share Contact", request_contact=True)
    button2 = KeyboardButton(text="Locate", request_location=True)
    button3 = KeyboardButton(text="/checksubscription")
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, greeting_text, reply_markup=keyboard)


def get_channel_members(message):
    return [message.chat.id]


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    bot.send_message(message.chat.id, f"Thank you! Please subs to this channel: https://t.me/sublinkchannel "
                                      f"\nThen press Subs check")


# @bot.message_handler(commands=['checksubscription'])
# def subscribe_check(message):
#     if message.chat.id in get_channel_members(message):
#         bot.send_message(message.chat.id, f"Thank you!")
#     else:
#         bot.send_message(message.chat.id, f"You are not subscribed to this channel")

@bot.message_handler(commands=['checksubscription'])
def check_subscription(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = "@sublinkchannel"
    try:
        member = context.bot.(chat_id, user_id)
        if member.status in ["member", "administrator", "creator"]:
            update.message.reply_text("You are a subscriber of the channel")
        else:
            update.message.reply_text("You are not a subscriber of the channel")
    except Exception as e:
        print(e)
        update.message.reply_text("An error occurred while checking subscription status.")


if __name__ == "__main__":
    bot.polling(none_stop=True)
