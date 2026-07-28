import psycopg2
def connectDB(dbname, uname, psw):...
conn = psycopg2.connect(database=dbname, user=uname, password=psw, host=
    '127.0.0.1', port='5432')
return conn
