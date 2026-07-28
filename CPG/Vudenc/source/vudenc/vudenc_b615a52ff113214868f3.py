def getCommentsByUser(self, userid):...
sqlText = (
    'select comment from comments order by date desc where userid=%d' % userid)
result = sql.queryDB(self.conn, sqlText)
return result
