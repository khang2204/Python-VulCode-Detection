def getUsersByName(self, userid, username):...
sqlText = (
    "select userid,name,country,(select Count(*) from friends                 where users.userid=friends.friendid and friends.userid=%d) as follow                 from users where users.name='%s';"
     % (userid, username))
result = sql.queryDB(self.conn, sqlText)
return result
