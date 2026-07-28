from python_version_check import check_version
check_version((3, 4, 3))
VERSION_NUMBER = 1, 0, 10
import logging
from random import choice
from time import time
import requests, json
from threading import Thread
from queue import Queue
from traceback_printer import full_traceback
from telegramHigh import TelegramHigh
from textual_data import *
from userparams import UserParams
from language_support import LanguageSupport
import utils
from file_db import FileDB
from button_handler import getMainMenu
from settings_reader import SettingsReader
sr = SettingsReader()
FILE_UPDATE_PERIOD = sr.settings_reader(0)
FROM_DROPBOX = bool(sr.settings_reader(2) == 'DB')
MIN_PICTURE_SEND_PERIOD = 60
MAX_PICTURE_SEND_PERIOD = 86400
PICTURE_SEND_PERIOD = sr.settings_reader(1)
INITIAL_SUBSCRIBER_PARAMS = {'lang': 'EN', 'subscribed': 0, 'period':
    PICTURE_SEND_PERIOD, 'last_update_time': 0}
"""The bot class"""
LAST_UPDATE_ID = None
pic_sender_threads = {}
def __init__(self, token):...
super(MainPicSender, self).__init__()
self.bot = TelegramHigh(token)
self.userparams = UserParams('users', initial=INITIAL_SUBSCRIBER_PARAMS)
self.file_db = FileDB('files')
self.updateFileListThread()
self.files = []
self.bot.start(processingFunction=self.processUpdate, periodicFunction=self
    .periodicRoutine)
def processUpdate(self, u):...
bot = self.bot
Message = u.message
message = Message.text
message_id = Message.message_id
chat_id = Message.chat_id
subs = self.userparams
subs.initializeUser(chat_id=chat_id, data=INITIAL_SUBSCRIBER_PARAMS)
LS = LanguageSupport(subs.getEntry(chat_id=chat_id, param='lang'))
lS = LS.languageSupport
allv = LS.allVariants
MMKM = lS(getMainMenu(subs.getEntry(chat_id=chat_id, param='subscribed')))
if message == '/start':
bot.sendMessage(chat_id=chat_id, message=lS(START_MESSAGE), key_markup=MMKM)
if message == '/help' or message == HELP_BUTTON:
def periodicRoutine(self):...
bot.sendMessage(chat_id=chat_id, message=lS(HELP_MESSAGE).format(str(
    MIN_PICTURE_SEND_PERIOD), str(MAX_PICTURE_SEND_PERIOD)), key_markup=
    MMKM, markdown=True)
if message == '/about' or message == ABOUT_BUTTON:
"""docstring"""
bot.sendMessage(chat_id=chat_id, message=lS(ABOUT_MESSAGE).format('.'.join(
    [str(i) for i in VERSION_NUMBER])), key_markup=MMKM, markdown=True)
if message == '/otherbots' or message == lS(OTHER_BOTS_BUTTON):
if not hasattr(self, 'update_filelist_thread_queue'):
bot.sendMessage(chat_id=chat_id, message=lS(OTHER_BOTS_MESSAGE), key_markup
    =MMKM, markdown=True)
if message == '/period' or message == lS(SHOW_PERIOD_BUTTON):
self.update_filelist_thread_queue = Queue()
while not self.update_filelist_thread_queue.empty():
period = self.userparams.getEntry(chat_id, 'period')
if message == '/subscribe' or message == SUBSCRIBE_BUTTON:
q = self.update_filelist_thread_queue.get()
self.updateFileListThread()
bot.sendMessage(chat_id=chat_id, message=
    'An image is sent to you every {0} seconds.'.format(period), key_markup
    =MMKM)
period = self.userparams.getEntry(chat_id, 'period')
if message == '/unsubscribe' or message == UNSUBSCRIBE_BUTTON:
self.last_filelist_update_time = q[0]
for user in self.userparams.getAllEntries(fields=['subscribed', 'period',
if self.userparams.getEntry(chat_id, 'subscribed') == 0:
if self.userparams.getEntry(chat_id, 'subscribed') == 1:
if message == '/gimmepic' or message == GIMMEPIC_BUTTON:
if user[0] == 1:
def updateFileListThread(self):...
self.userparams.setEntry(chat_id, 'subscribed', 1)
bot.sendMessage(chat_id=chat_id, message=
    """You have already subscribed!
To cancel subscription enter /unsubscribe.
To change the period of picture sending type a number.
Your current period is {0} seconds."""
    .format(period), key_markup=MMKM)
self.userparams.setEntry(chat_id, 'subscribed', 0)
bot.sendMessage(chat_id=chat_id, message=
    "You haven't subscribed yet! To subscribe type /subscribe", key_markup=MMKM
    )
self.startRandomPicThread(chat_id, MMKM)
new_period = int(message)
bot.sendMessage(chat_id=chat_id, message='Unknown command!', key_markup=MMKM)
cur_time = time()
"""docstring"""
self.userparams.setEntry(chat_id, 'last_update_time', time())
MMKM = getMainMenu(subscribed=False)
if self.userparams.getEntry(chat_id, 'subscribed') == 0:
if cur_time - user[2] > user[1]:
if not hasattr(self, 'last_filelist_update_time') or time(
MMKM = getMainMenu(subscribed=True)
bot.sendMessage(chat_id=chat_id, message=
    'You have unsubscribed. To subscribe again type /subscribe', key_markup
    =MMKM)
bot.sendMessage(chat_id=chat_id, message=
    "You're not subscribed yet! /subscribe first!", key_markup=MMKM)
if new_period < MIN_PICTURE_SEND_PERIOD:
self.startRandomPicThread(user[3], MMKM=getMainMenu(True))
if not (hasattr(self, 'filelist_updater_thread') and self.
def fileToDB(self, filepath, mod_time):...
bot.sendMessage(chat_id=chat_id, message=
    """You're subscribed now! 
An image will be sent to you every {0} seconds. 
To cancel subscription enter /unsubscribe. 
To change the period of picture sending type a number."""
    .format(period), key_markup=MMKM)
self.userparams.setEntry(chat_id, 'period', MIN_PICTURE_SEND_PERIOD)
if new_period > MAX_PICTURE_SEND_PERIOD:
self.userparams.setEntry(user[3], 'last_update_time', cur_time)
self.filelist_updater_thread = Thread(target=self.updateFileList)
print('updater already running!')
"""docstring"""
bot.sendMessage(chat_id=chat_id, message=
    """The minimum possible period is {0}.
Setting period to {0}.""".format
    (str(MIN_PICTURE_SEND_PERIOD)), key_markup=MMKM)
self.userparams.setEntry(chat_id, 'period', MAX_PICTURE_SEND_PERIOD)
self.userparams.setEntry(chat_id, 'period', new_period)
self.filelist_updater_thread.start()
file_db = self.file_db
self.userparams.setEntry(chat_id, 'last_update_time', int(time()))
bot.sendMessage(chat_id=chat_id, message=
    """The maximum possible period is {0}.
Setting period to {0}.""".format
    (str(MAX_PICTURE_SEND_PERIOD)), key_markup=MMKM)
bot.sendMessage(chat_id=chat_id, message='Setting period to ' + str(
    new_period) + '.', key_markup=MMKM)
if path.splitext(filepath)[1].replace('.', '').lower() != 'txt':
if not file_db.fileExists(filepath):
if path.basename(filepath) == METADATA_FILENAME:
file_db.addFile(filepath, mod_time=mod_time)
if mod_time > file_db.getModTime(filepath):
def getMetadata():...
def checkFilesForDeletion(self, files):...
file_db.invalidateCached(filepath)
metadata = ''
"""docstring"""
file_db.updateModTime(filepath, mod_time)
if not FROM_DROPBOX:
logging.error('Could not read metafile!', full_traceback())
return metadata
file_db = self.file_db
metadata = f.read()
metadata = self.getDropboxFile(filepath).decode()
DB_files = file_db.getFileList()
for f in DB_files:
if not f in files:
def updateFileList(self):...
file_db.deleteFile(f)
"""docstring"""
if not FROM_DROPBOX:
files = utils.FolderSearch.getFilepathsInclSubfolders(PIC_FOLDER,
    allowed_extensions=['txt', 'png', 'jpg', 'jpeg'])
files_and_mods = (utils.DropboxFolderSearch.
    getFilepathsInclSubfoldersDropboxPublic(DROPBOX_FOLDER_LINK,
    DROPBOX_APP_KEY, DROPBOX_SECRET_KEY, unixify_mod_time=True))
files_and_mods = list(zip(files, [utils.FileUtils.getModificationTimeUnix(f
    ) for f in files]))
files = [i[0] for i in files_and_mods]
for i in files_and_mods:
self.fileToDB(i[0], i[1])
self.checkFilesForDeletion(files)
last_filelist_update_time = time()
self.update_filelist_thread_queue.put((last_filelist_update_time,))
@staticmethod...
"""docstring"""
data = None
req = requests.post('https://api.dropbox.com/1/metadata/link', data=dict(
    link=DROPBOX_FOLDER_LINK, client_id=DROPBOX_APP_KEY, client_secret=
    DROPBOX_SECRET_KEY, path=filepath), timeout=5)
if req.ok:
req = json.loads(req.content.decode())['link'].split('?')[0] + '?dl=1'
data = None
req = requests.get(req, timeout=5)
data = None
return data
if req.ok:
data = req.content
