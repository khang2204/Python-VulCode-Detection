def insertData(self, comment, userid, postid):...
sqlText = (
    "insert into comments(comment,userid,date,postid) values('%s',%d,current_timestamp(0),%d);"
     % (comment, userid, postid))
result = sql.insertDB(self.conn, sqlText)
return result
