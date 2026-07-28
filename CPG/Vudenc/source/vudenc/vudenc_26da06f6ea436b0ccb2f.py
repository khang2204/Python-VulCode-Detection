def isMultiChoice(poll_name):...
conn, c = connectDB()
req = "SELECT multi FROM {} WHERE name = '{}'".format(CFG('poll_table_name'
    ), poll_name)
ret = queryOne(c, req) == 1
closeDB(conn)
return ret
