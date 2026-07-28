def add_phrase(self, aphrase, database='main', commit=True):...
"""docstring"""
input_phrase, phrase, freq, user_freq = aphrase
input_phrase, phrase, freq = aphrase
select_sqlstr = (
    """
        SELECT * FROM %(database)s.phrases
        WHERE input_phrase = :input_phrase AND phrase = :phrase
        ;"""
     % {'database': database})
user_freq = 0
select_sqlargs = {'input_phrase': input_phrase, 'phrase': phrase}
if self.db.execute(select_sqlstr, select_sqlargs).fetchall():
return
insert_sqlstr = (
    """
        INSERT INTO %(database)s.phrases
        (mlen, clen, input_phrase, phrase, freq, user_freq)
        VALUES ( :mlen, :clen, :input_phrase, :phrase, :freq, :user_freq)
        ;"""
     % {'database': database})
insert_sqlargs = {'mlen': len(input_phrase), 'clen': len(phrase),
    'input_phrase': input_phrase, 'phrase': phrase, 'freq': freq,
    'user_freq': user_freq}
self.db.execute(insert_sqlstr, insert_sqlargs)
import traceback
if commit:
traceback.print_exc()
self.db.commit()
