"""
Small bot for Telegram that receives your photo and returns you map where
it was taken.
Written by Aleksandr Mikheev.
https://github.com/RandyRomero/photogpsbot

This specific module contains methods to respond user messages, to make
interactive menus, to handle user language, to process user images
"""
from io import BytesIO
from datetime import datetime, timedelta
from telebot import types
import requests
from photogpsbot import bot, log, log_files, db, User, users, messages, machine
from photogpsbot.process_image import ImageHandler
from photogpsbot.db_connector import DatabaseConnectionError
import config
def __init__(self, message, user):...
self.message = message
self.user = user
self.image_handler = ImageHandler
@staticmethod...
file_path = bot.get_file(message.document.file_id).file_path
link = f'https://api.telegram.org/file/bot{config.TELEGRAM_TOKEN}/{file_path}'
if machine == 'prod':
r = requests.get(link)
proxies = {'https': config.PROXY_CONFIG}
return BytesIO(r.content)
r = requests.get(link, proxies=proxies)
