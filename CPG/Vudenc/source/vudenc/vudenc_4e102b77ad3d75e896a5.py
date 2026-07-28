def startThread(chat_id):...
t = Thread(target=self.sendRandomPic, args=(chat_id, MMKM))
self.pic_sender_threads[chat_id] = t
t.start()
