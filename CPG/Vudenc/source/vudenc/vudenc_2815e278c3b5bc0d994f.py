def genTokensExternal(poll_name, count=False):...
conn, c = connectDB()
tok = genTokens(c, poll_name, count)
closeDB(conn)
return tok
