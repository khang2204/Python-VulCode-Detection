def create_indexes(self, database, commit=True):...
sqlstr = (
    """
            CREATE INDEX IF NOT EXISTS %(database)s.phrases_index_p ON phrases
            (input_phrase, mlen ASC, freq DESC, id ASC);
            CREATE INDEX IF NOT EXISTS %(database)s.phrases_index_i ON phrases
            (phrase, mlen ASC);"""
     % {'database': database})
self.db.executescript(sqlstr)
if commit:
self.db.commit()
