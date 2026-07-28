def create_tables(self, database):...
"""docstring"""
self.db.execute('PRAGMA cache_size = 20000; ')
sqlstr = (
    """CREATE TABLE IF NOT EXISTS %s.phrases
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    mlen INTEGER, clen INTEGER,
                    input_phrase TEXT, phrase TEXT,
                    freq INTEGER, user_freq INTEGER);"""
     % database)
self.db.execute(sqlstr)
self.db.commit()
