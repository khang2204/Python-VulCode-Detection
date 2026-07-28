def getAllInformation(self, userid):...
sqlText = ('select name,password,email,country from users where userid=%d;' %
    userid)
information = sql.queryDB(self.conn, sqlText)
return information
