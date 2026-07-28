def getAllPosts(self):...
sqlText = 'select comment from post where userid=%d order by date;'
allposts = sql.queryDB(self.conn, sqlText)
return allposts
