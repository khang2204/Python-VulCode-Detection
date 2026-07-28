def tokenNeededExternal(poll_name):...
conn, c = connectDB()
tmp = checkTokenNeeded(c, poll_name)
conn.close()
return tmp
