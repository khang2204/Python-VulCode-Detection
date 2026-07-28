"""
Module to manage users of bot: store and update information, interact with
the database, keep tack of and switch language of interface for user
"""
import config
from photogpsbot import bot, log, db
from photogpsbot.db_connector import DatabaseError, DatabaseConnectionError
from telebot.types import Message
"""
    Class that describes one user of this Telegram bot and helps to store basic
    info about him and his language of choice for interface of the bot
    """
def __init__(self, chat_id, first_name, nickname, last_name, language='en-US'):...
self.chat_id = chat_id
self.first_name = first_name
self.nickname = nickname
self.last_name = last_name
self.language = language
def set_language(self, lang):...
"""docstring"""
log.debug('Updating info about user %s language in memory & database...', self)
self.language = lang
query = (
    f"UPDATE users SET language='{self.language}' WHERE chat_id='{self.chat_id}'"
    )
db.add(query)
log.error("Can't add new language of %s to the database", self)
log.debug('Language updated.')
def switch_language(self):...
"""docstring"""
curr_lang = self.language
new_lang = 'ru-RU' if self.language == 'en-US' else 'en-US'
log.info('Changing user %s language from %s to %s...', self, curr_lang,
    new_lang)
self.set_language(new_lang)
return new_lang
