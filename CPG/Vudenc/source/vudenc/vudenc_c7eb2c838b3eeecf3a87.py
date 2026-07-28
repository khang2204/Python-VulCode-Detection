def userApply(self):...
t_sql_insert = (
    "insert into                 users(name,password,email,country,inscription_date)                 values('{name}','{psw}','{email}','{country}',current_timestamp(0));"
    )
sql_insert = t_sql_insert.format(name=self.name, psw=self.password, email=
    self.email, country=self.country)
sqlName = "select count(*) from users where name='%s';" % self.name
checkName = sql.queryDB(self.conn, sqlName)
if checkName[0][0] == 0:
sql.insertDB(self.conn, sql_insert)
return False
return True
