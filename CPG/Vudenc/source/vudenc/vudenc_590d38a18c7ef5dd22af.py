def delete(self, targetWord):...
self.connect()
sqlFormula = "DELETE FROM badwords WHERE word='%s'" % targetWord
self.cursor.execute(sqlFormula)
self.close()
