def optimize_database(self, database='main'):...
sqlstr = (
    """
            CREATE TABLE tmp AS SELECT * FROM %(database)s.phrases;
            DELETE FROM %(database)s.phrases;
            INSERT INTO %(database)s.phrases SELECT * FROM tmp ORDER BY
            input_phrase, mlen ASC, user_freq DESC, freq DESC, id ASC;
            DROP TABLE tmp;"""
     % {'database': database})
self.db.executescript(sqlstr)
self.db.executescript('VACUUM;')
self.db.commit()
