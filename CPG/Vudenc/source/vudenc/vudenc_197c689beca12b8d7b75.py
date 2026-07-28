def remove_phrase(self, phrase, database='user_db'):...
"""docstring"""
id, mlen, clen, input_phrase, phrase, freq, user_freq = phrase
delete_sqlstr = (
    """
        DELETE FROM %(database)s.phrases
        WHERE input_phrase = :input_phrase AND phrase = :phrase
        ;"""
     % {'database': database})
delete_sqlargs = {'input_phrase': input_phrase, 'phrase': phrase}
self.db.execute(delete_sqlstr, delete_sqlargs)
self.db.commit()
