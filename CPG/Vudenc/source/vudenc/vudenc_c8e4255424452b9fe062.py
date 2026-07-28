def checkTokenNeeded(cursor, poll_name):...
req = "SELECT has_tokens FROM {} WHERE name = '{}'".format(CFG(
    'poll_table_name'), poll_name)
return queryOne(cursor, req) == 1
