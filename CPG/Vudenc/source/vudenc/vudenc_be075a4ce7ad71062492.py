from modules import sql
def __init__(self, conn):...
self.conn = conn
def getCommentsByUser(self, userid):...
sqlText = (
    'select comment from comments order by date desc where userid=%d' % userid)
result = sql.queryDB(self.conn, sqlText)
return result
