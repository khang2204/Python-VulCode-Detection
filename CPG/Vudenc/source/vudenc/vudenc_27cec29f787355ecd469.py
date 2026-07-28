def getOptionCount(c, poll_name, option):...
key = poll_name + '-' + option
req = 'SELECT "count" FROM {table} WHERE "name_option" = \'{key}\''.format(
    table=CFG('options_table_name'), key=key)
count = queryOne(c, req)
if count == None:
return count
