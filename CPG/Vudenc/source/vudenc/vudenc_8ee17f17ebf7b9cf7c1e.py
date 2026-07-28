def checkAdmTokenValid(poll_name, adm_token):...
conn, c = connectDB()
req = 'SELECT poll_name from {} where adm_token = "{}"'.format(CFG(
    'admintoken_table_name'), adm_token)
answer = queryOne(c, req)
closeDB(conn)
return answer == poll_name
