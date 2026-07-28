def connect(self):...
self.mydb = mysql.connector.connect(host=self.host, user=self.user, passwd=
    self.passwd, database=self.database)
self.cursor = self.mydb.cursor()
