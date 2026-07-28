def getAdmToken(poll_name):...
conn, c = connectDB()
req = "SELECT adm_token FROM {} WHERE poll_name='{}'".format(CFG(
    'admintoken_table_name'), poll_name)
admtok = queryOne(c, req)
closeDB(conn)
return admtok
