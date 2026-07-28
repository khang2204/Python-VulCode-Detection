def isValidToken(token):...
conn, c = connectDB()
req = "SELECT * from {} where token='{}'".format(CFG('tokens_table_name'),
    token)
answer = bool(queryOne(c, req))
closeDB(conn)
return answer
