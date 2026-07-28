def likePost(self, postid, userid):...
sqlText = 'insert into post_like values(%d,%d);' % (postid, userid)
result = sql.insertDB(self.conn, sqlText)
return result
