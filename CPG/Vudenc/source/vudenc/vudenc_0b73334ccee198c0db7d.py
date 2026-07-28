def getTokensExternal(poll_name):...
req = "SELECT token FROM {} WHERE name='{}'".format(CFG('tokens_table_name'
    ), poll_name)
conn, c = connectDB()
tmp = queryAll(c, req)
conn.close()
return tmp
