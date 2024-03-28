import time

import telebot

from telegram import Update
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from telegram.ext import CallbackContext

from telegram.ext import Updater, CommandHandler, CallbackContext
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6750835343:AAG8AbiQphxwT7L-EIea3l4Dcfo9C1GQZe4'
bot = telebot.TeleBot(TOKEN)

user_data = {}


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
    button4 = KeyboardButton(text="/friend")
    keyboard.add(button1, button2, button3, button4)

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
    referral_link = f"https://t.me/linkercheck_bot?start={user_id}"
    try:
        member = bot.get_chat_member(channel_id, user_id)
        if member.status == 'member' or member.status == 'creator':
            # print("Subscribed")

            bot.send_message(message.chat.id, f"Congratulations! Wait a link of the group!")
            # time.sleep(6)
            bot.send_message(message.chat.id, f"Subscribe to {private_group_id}")

            bot.send_message(message.chat.id, f"Share with 5 friends {referral_link}")
            # time.sleep(6)
            # bot.send_message(message.chat.id, f"Subscribe to {private_group_id}")

        else:
            # print("Unsubscribed")
            bot.send_message(message.chat.id, f"You have to subscribe to the channel at first. PLease share contact!")
    except Exception as e:
        # print("Error while subscribing", e)
        bot.send_message(message.chat.id, f"Oops something went wrong. Please try again later")


@bot.message_handler(commands=['friend'])
def referral_link_click(update, context):
    user_id = update.effective_user.id
    referred_by = update.effective_message.text.split()[-1]
    if user_id not in user_data:
        user_data[user_id] = {"referral_count": 0, "referred_by": referred_by}
    user_data[user_id]["referral_count"] += 1
    if user_data[user_id]["referral_count"] >= 2:
        context.bot.send_message(chat_id=user_id,
                                 text="You've reached 5 referrals")


if __name__ == "__main__":
    bot.polling(none_stop=True)
