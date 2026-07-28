import sys
import pymysql
import pymysql.cursors
import dbconfig
def connects(self, database='crimemap'):...
conn = pymysql.connect(host='localhost', user=dbconfig.db_user, password=
    dbconfig.db_password, db=database, charset='utf8mb4', cursorclass=
    pymysql.cursors.DictCursor)
print(e)
return conn
