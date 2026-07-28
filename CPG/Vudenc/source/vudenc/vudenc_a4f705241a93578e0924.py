def extract_user_phrases(self, udb, only_defined=False):...
"""docstring"""
db = sqlite3.connect(udb)
return None
if only_defined:
_phrases = db.execute(
    'SELECT clen, phrase, freq, sum(user_freq)                    FROM phrases                     WHERE freq=-1 AND mlen != 0                     GROUP BY clen,phrase;'
    ).fetchall()
_phrases = db.execute(
    'SELECT clen, phrase, freq, sum(user_freq)                    FROM phrases                    WHERE mlen !=0                     GROUP BY clen,phrase;'
    ).fetchall()
db.commit()
return _phrases[:]
