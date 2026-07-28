def pollNameFromToken(token):...
conn, c = connectDB()
req = "SELECT name from {} where token='{}'".format(CFG('tokens_table_name'
    ), token)
answer = queryOne(c, req)
if not answer:
req = "SELECT poll_name from {} where adm_token='{}'".format(CFG(
    'admintoken_table_name'), token)
closeDB(conn)
answer = queryOne(c, req)
return answer
