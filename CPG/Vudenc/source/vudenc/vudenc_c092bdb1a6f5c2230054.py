def connect(self, hostname='localhost', username='todo', password='todo',...
"""docstring"""
self.__con = MySQLdb.connect(hostname, username, password, database)
return Database.CANT_CONNECT
self.__con.autocommit(True)
return Database.SUCCESS
