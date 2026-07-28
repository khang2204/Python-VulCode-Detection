def getUsers(self, userid):...
sqlText = (
    'select userid,name,country,(select Count(*) from friends                 where users.userid=friends.friendid and friends.userid=%d) as follow                 from users;'
     % userid)
result = sql.queryDB(self.conn, sqlText)
return result
