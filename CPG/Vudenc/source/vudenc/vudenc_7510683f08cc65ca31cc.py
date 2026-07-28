def getResults(poll_name):...
conn, c = connectDB()
req = "SELECT options from {} where name = '{}'".format(CFG(
    'poll_table_name'), poll_name)
options_str = queryOne(c, req)
if not options_str:
total = 0
options = options_str.split(',')
results = dict()
for opt in options:
count = getOptionCount(c, poll_name, opt)
conn.close()
total += int(count)
return results, total
results.update({opt: count})
