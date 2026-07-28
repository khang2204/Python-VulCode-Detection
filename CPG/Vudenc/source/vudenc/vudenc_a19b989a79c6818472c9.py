def __db_connect__(self):...
self.db = sqlite3.connect(self.db_name)
self.db.row_factory = sqlite3.Row
self.cursor = self.db.cursor()
