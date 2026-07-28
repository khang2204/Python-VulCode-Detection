def update_phrase(self, entry, database='user_db'):...
"""docstring"""
input_phrase, phrase, freq, user_freq = entry
sqlstr = (
    """UPDATE %(database)s.phrases
                    SET user_freq = %(user_freq)s
                    WHERE mlen = %(mlen)s
                    AND clen = %(clen)s
                    AND input_phrase = "%(input_phrase)s"
                    AND phrase = "%(phrase)s";
        """
     % {'database': database, 'user_freq': user_freq, 'mlen': len(
    input_phrase), 'clen': len(phrase), 'input_phrase': input_phrase,
    'phrase': phrase})
self.db.execute(sqlstr)
self.db.commit()
