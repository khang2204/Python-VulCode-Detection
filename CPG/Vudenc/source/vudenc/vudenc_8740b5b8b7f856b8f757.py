def connect(self):...
"""docstring"""
create_table = not os.path.exists(HistoryDB.db_path)
self.con = sqlite3.connect(HistoryDB.db_path)
self.con.row_factory = dict_factory
self.c = self.con.cursor()
if create_table:
self.create_history_db()
if not HistoryDB.done_cleaning:
self.execute('PRAGMA user_version;')
HistoryDB.done_cleaning = True
version = self.c.fetchone()['user_version']
version = 0
if version < 1:
self.execute('VACUUM')
_ = self.execute('PRAGMA user_version = 1;') and self.execute(
    'ALTER TABLE "history" ADD COLUMN series TEXT;') and self.execute(
    'ALTER TABLE "history" ADD COLUMN md5sum TEXT;')
if version < 2:
_ = self.execute('PRAGMA user_version = 2;') and self.execute(
    'ALTER TABLE "history" ADD COLUMN password TEXT;')
