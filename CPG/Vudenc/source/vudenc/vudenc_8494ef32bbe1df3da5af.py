def deleteComment(self, commentid):...
sqlText = 'delete from comments where commentid=%d' % commentid
result = sql.deleteDB(self.conn, sqlText)
return result
