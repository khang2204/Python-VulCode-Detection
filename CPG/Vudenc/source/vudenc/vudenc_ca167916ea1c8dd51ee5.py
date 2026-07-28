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
bot.sendMessage(chat_id=chat_id, message=lS(HELP_MESSAGE).format(str(
    MIN_PICTURE_SEND_PERIOD), str(MAX_PICTURE_SEND_PERIOD)), key_markup=
    MMKM, markdown=True)
if message == '/about' or message == ABOUT_BUTTON:
bot.sendMessage(chat_id=chat_id, message=lS(ABOUT_MESSAGE).format('.'.join(
    [str(i) for i in VERSION_NUMBER])), key_markup=MMKM, markdown=True)
if message == '/otherbots' or message == lS(OTHER_BOTS_BUTTON):
bot.sendMessage(chat_id=chat_id, message=lS(OTHER_BOTS_MESSAGE), key_markup
    =MMKM, markdown=True)
if message == '/period' or message == lS(SHOW_PERIOD_BUTTON):
period = self.userparams.getEntry(chat_id, 'period')
if message == '/subscribe' or message == SUBSCRIBE_BUTTON:
bot.sendMessage(chat_id=chat_id, message=
    'An image is sent to you every {0} seconds.'.format(period), key_markup
    =MMKM)
period = self.userparams.getEntry(chat_id, 'period')
if message == '/unsubscribe' or message == UNSUBSCRIBE_BUTTON:
if self.userparams.getEntry(chat_id, 'subscribed') == 0:
if self.userparams.getEntry(chat_id, 'subscribed') == 1:
if message == '/gimmepic' or message == GIMMEPIC_BUTTON:
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
self.userparams.setEntry(chat_id, 'last_update_time', time())
MMKM = getMainMenu(subscribed=False)
if self.userparams.getEntry(chat_id, 'subscribed') == 0:
MMKM = getMainMenu(subscribed=True)
bot.sendMessage(chat_id=chat_id, message=
    'You have unsubscribed. To subscribe again type /subscribe', key_markup
    =MMKM)
bot.sendMessage(chat_id=chat_id, message=
    "You're not subscribed yet! /subscribe first!", key_markup=MMKM)
if new_period < MIN_PICTURE_SEND_PERIOD:
bot.sendMessage(chat_id=chat_id, message=
    """You're subscribed now! 
An image will be sent to you every {0} seconds. 
To cancel subscription enter /unsubscribe. 
To change the period of picture sending type a number."""
    .format(period), key_markup=MMKM)
self.userparams.setEntry(chat_id, 'period', MIN_PICTURE_SEND_PERIOD)
if new_period > MAX_PICTURE_SEND_PERIOD:
bot.sendMessage(chat_id=chat_id, message=
    """The minimum possible period is {0}.
Setting period to {0}.""".format
    (str(MIN_PICTURE_SEND_PERIOD)), key_markup=MMKM)
self.userparams.setEntry(chat_id, 'period', MAX_PICTURE_SEND_PERIOD)
self.userparams.setEntry(chat_id, 'period', new_period)
self.userparams.setEntry(chat_id, 'last_update_time', int(time()))
bot.sendMessage(chat_id=chat_id, message=
    """The maximum possible period is {0}.
Setting period to {0}.""".format
    (str(MAX_PICTURE_SEND_PERIOD)), key_markup=MMKM)
bot.sendMessage(chat_id=chat_id, message='Setting period to ' + str(
    new_period) + '.', key_markup=MMKM)
