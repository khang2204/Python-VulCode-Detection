def startRandomPicThread(self, chat_id, MMKM):...
"""docstring"""
def startThread(chat_id):...
t = Thread(target=self.sendRandomPic, args=(chat_id, MMKM))
self.pic_sender_threads[chat_id] = t
t.start()
if not self.pic_sender_threads[chat_id].isAlive():
startThread(chat_id)
startThread(chat_id)
self.bot.sendMessage(chat_id=chat_id, message=
    "I'm still sending you a pic. Please wait!")
