def fetch(self):...
self.connect()
sqlFormula = 'SELECT * FROM badwords'
self.cursor.execute(sqlFormula)
myresults = self.cursor.fetchall()
badWordArray = []
for row in myresults:
badWordArray.append(row[0])
self.close()
return badWordArray
