def checkTokenValid(cursor, token, poll_name):...
req = "SELECT name, options_selected from {} where token='{}'".format(CFG(
    'tokens_table_name'), token)
answer = queryAll(cursor, req)
return answer and answer[0][0] == poll_name and answer[0][1] == 'NONE'
