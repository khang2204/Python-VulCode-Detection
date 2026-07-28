def dislikePost(self, postid, userid):...
sqlText = 'delete from post_like where postid=%d and userid=%d;' % (postid,
    userid)
result = sql.deleteDB(self.conn, sqlText)
return result
