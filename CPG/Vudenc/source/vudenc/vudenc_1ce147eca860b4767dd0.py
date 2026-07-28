def __init__(self, config):...
self.config = config
self.db = sqlite3.connect(self.config.get_database_path(),
    check_same_thread=False)
self.c = self.db.cursor()
