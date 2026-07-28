def dislikeComments(self, commentid, userid):...
sqlText = 'delete from comment_like where commentid=%d and userid=%d;' % (
    commentid, userid)
result = sql.deleteDB(self.conn, sqlText)
return result
