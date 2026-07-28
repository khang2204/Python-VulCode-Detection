def getUserID(self):...
sqlName = "select userid from users where name='%s';" % self.name
userid = sql.queryDB(self.conn, sqlName)
return userid[0][0]
