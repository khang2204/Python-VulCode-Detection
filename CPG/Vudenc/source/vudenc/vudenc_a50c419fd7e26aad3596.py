def insert(self, targetWord, badwordlist):...
if not targetWord.lower() in badwordlist:
self.connect()
sqlFormula = 'INSERT INTO badwords (word, badness) VALUE (%s,%s)'
word = targetWord.lower(), 1
self.cursor.execute(sqlFormula, word)
self.close()
