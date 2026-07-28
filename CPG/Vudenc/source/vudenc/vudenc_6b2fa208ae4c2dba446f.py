def drop_indexes(self, database):...
"""docstring"""
sqlstr = (
    """
            DROP INDEX IF EXISTS %(database)s.phrases_index_p;
            DROP INDEX IF EXISTS %(database)s.phrases_index_i;
            VACUUM;
            """
     % {'database': database})
self.db.executescript(sqlstr)
self.db.commit()
