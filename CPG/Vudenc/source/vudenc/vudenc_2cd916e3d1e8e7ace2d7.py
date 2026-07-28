@gen.coroutine...
args = {}
args['host'] = self.dbhost
args['user'] = self.dbuser
args['password'] = self.dbpassword
args['db'] = self.dbname
args['charset'] = 'utf8mb4'
args['cursorclass'] = pymysql.cursors.Cursor
sql = 'SELECT user_pass FROM {0}users WHERE user_login = "{1}"'.format(self
    .table_prefix, data['username'])
if cursor.execute(sql) == 0:
return None
if phpass.verify(data['password'], cursor.fetchone()[0]) == True:
return data['username']
return None
