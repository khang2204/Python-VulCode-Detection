def __init__(self, token):...
super(MainPicSender, self).__init__()
self.bot = TelegramHigh(token)
self.userparams = UserParams('users', initial=INITIAL_SUBSCRIBER_PARAMS)
self.file_db = FileDB('files')
self.updateFileListThread()
self.files = []
self.bot.start(processingFunction=self.processUpdate, periodicFunction=self
    .periodicRoutine)
