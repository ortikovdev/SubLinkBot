import sqlite3
import time

import telebot

from telegram import Update
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from telegram.ext import Updater, CommandHandler, CallbackContext
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


TOKEN = '6750835343:AAG8AbiQphxwT7L-EIea3l4Dcfo9C1GQZe4'
bot = telebot.TeleBot(TOKEN)

# conn = sqlite3.connect('videos.db')
# cursor = conn.cursor()

user_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    greeting_text = f"Hello, {user_name}! 👋\n\nPlease share your contact"

    # Create a custom keyboard with a "Share Contact" button
    keyboard = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True, is_persistent=True)
    # keyboard = [[InlineKeyboardButton("Watch Video", callback_data='watch_video')]]
    button1 = KeyboardButton(text="Share Contact", request_contact=True)
    button2 = KeyboardButton(text="Watch Video")
    button3 = KeyboardButton(text="/check")
    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, greeting_text, reply_markup=keyboard)


# CHANNELUSER = "https://t.me/+nvovNsvJC_gzYjg6"


# def get_channel_videos(channel_username):
#     try:
#         messages = bot.get_updates(chat_id=-1002034404872)
#         print(messages)
#         videos = []
#         for message in messages:
#             if message.video is not None:
#                 videos.append(message.video)
#         return videos
#     except Exception as e:
#         print("Error getting channel videos", e)
#         return []


@bot.message_handler(func=lambda message: message.text == "Watch Video")
def watch_video(message):
    video_link = "https://youtu.be/YTg4yuo1fA8"
    button = InlineKeyboardMarkup([[InlineKeyboardButton(text="Watch Video", url=video_link)]])
    bot.send_message(message.chat.id, 'Hi students. Here you will find some useful!', reply_markup=button)
    # videos = get_channel_videos(CHANNELUSER)
    # if videos:
    #     keyboard = InlineKeyboardMarkup(row_width=1)
    #     for video in videos:
    #         button = InlineKeyboardButton(text="Watch Video", url=video.get_file().file_path)
    #         keyboard.add(button)
    #
    #     bot.send_message(message.chat.id, "Here are some videos:", reply_markup=keyboard)
    # else:
    #     bot.send_message(message.chat.id, "No videos")
    # bot.edit_message_reply_markup(message.chat.id, "Here's the vieo link:")

    # button = InlineKeyboardMarkup(text="Watch Video", url=video_link)
    # keyboard.add(button)


# def get_channel_members(message):
#     return [message.chat.id]


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
            # bot.send_message(message.chat.id, f"Subscribe to {private_group_id}")
            # bot.send_message(message.chat.id, f"Share with 5 friends {referral_link}")
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
