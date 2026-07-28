def queryQuestion(poll_name):...
conn, c = connectDB()
req = "SELECT question from {} WHERE name = '{}'".format(CFG(
    'poll_table_name'), poll_name)
tmp = queryOne(c, req)
conn.close()
return tmp
