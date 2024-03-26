import time

import telebot
from telegram import Update
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from telegram.ext import CallbackContext

from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '6750835343:AAG8AbiQphxwT7L-EIea3l4Dcfo9C1GQZe4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    greeting_text = f"Hello, {user_name}! 👋\n\nPlease share your contact"

    # Create a custom keyboard with a "Share Contact" button
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True, is_persistent=True)
    # keyboard = [[InlineKeyboardButton("Watch Video", callback_data='watch_video')]]
    button1 = KeyboardButton(text="Share Contact", request_contact=True)
    button2 = KeyboardButton(text="Watch Video")
    button3 = KeyboardButton(text="/check")
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, greeting_text, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Watch Video")
def watch_video(message):
    video_link = "https://www.youtube.com/watch?v=RV3IzFlylBw"
    # bot.edit_message_reply_markup(message.chat.id, "Here's the video link:")
    bot.send_message(message.chat.id, video_link)

# def get_channel_members(message):
#     return [message.chat.id]
#

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

@bot.message_handler(commands=['check'])
def check_subscription(message):
    user_id = message.from_user.id
    channel_id = "@sublinkchannel"
    private_group_id = "https://t.me/+e6HHxnz6iuZjNGNi"
    try:
        member = bot.get_chat_member(channel_id, user_id)
        if member.status == 'member' or member.status == 'creator':
            # print("Subscribed")
            bot.send_message(message.chat.id, f"Congratulations! Wait a link of the group!")
            # time.sleep(6)
            bot.send_message(message.chat.id, f"Subscribe to {private_group_id}")
        else:
            # print("Unsubscribed")
            bot.send_message(message.chat.id, f"You have to subscribe to the channel at first. PLease share contact!")
    except Exception as e:
        # print("Error while subscribing", e)
        bot.send_message(message.chat.id, f"Oops something went wrong. Please try again later")


if __name__ == "__main__":
    bot.polling(none_stop=True)
