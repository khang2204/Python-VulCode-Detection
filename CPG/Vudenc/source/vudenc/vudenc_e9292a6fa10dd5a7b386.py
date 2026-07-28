def insertOption(c, poll_name, option):...
key = poll_name + '-' + option
count = 0
params = key, count
req = 'INSERT INTO {} VALUES (?, ?)'.format(CFG('options_table_name'))
c.execute(req, params)
