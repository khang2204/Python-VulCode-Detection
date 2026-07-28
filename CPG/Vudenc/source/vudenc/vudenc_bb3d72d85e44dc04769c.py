import pymysql
def create_connection():...
connection = pymysql.connect(host='localhost', user='root', passwd='', db=
    'ebola')
print('connection error: ', error)
return connection
