def modifyUserInfo(self, userid, flag):...
sqlText = (
    "update users                 set name='%s',password='%s',email='%s',country='%s'                 where userid='%d';"
     % (self.name, self.password, self.email, self.country, userid))
if flag == 1:
sqlName = "select count(*) from users where name='%s';" % self.name
sql.updateDB(self.conn, sqlText)
checkName = sql.queryDB(self.conn, sqlName)
return True
if checkName[0][0] == 0:
sql.updateDB(self.conn, sqlText)
return False
return True
