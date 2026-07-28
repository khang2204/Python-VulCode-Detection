def init_user_db(self, db_file):...
if not path.exists(db_file):
db = sqlite3.connect(db_file)
db.execute('PRAGMA page_size = 4096;')
db.execute('PRAGMA cache_size = 20000;')
db.execute('PRAGMA temp_store = MEMORY; ')
db.execute('PRAGMA synchronous = OFF; ')
db.commit()
