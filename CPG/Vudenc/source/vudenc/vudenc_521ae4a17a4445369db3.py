import mysql.connector
from serverSetup import DBUSER, DBPASS
def __init__(self, host, user, passwd, database, filterList=[]):...
self.host = host
self.user = user
self.passwd = passwd
self.database = database
self.filterList = filterList
def connect(self):...
self.mydb = mysql.connector.connect(host=self.host, user=self.user, passwd=
    self.passwd, database=self.database)
self.cursor = self.mydb.cursor()
def close(self):...
self.cursor.close()
self.mydb.close()
def fetch(self):...
self.connect()
sqlFormula = 'SELECT * FROM badwords'
self.cursor.execute(sqlFormula)
myresults = self.cursor.fetchall()
badWordArray = []
for row in myresults:
badWordArray.append(row[0])
self.close()
return badWordArray
