def getPostLike(self, postid):...
sqlText = 'select userid from post_like where postid=%d' % postid
result = sql.queryDB(self.conn, sqlText)
return result
