import pymysql
import dbconfig
def connect(self, database='crimemap'):...
return pymysql.connect(host='localhost', user=dbconfig.db_user, passwd=
    dbconfig.db_password, db=database)
