def createPoll(poll_name, options_arr, question, has_tokens, multi,...
if checkPollExists(poll_name):
conn, c = connectDB()
name = poll_name
options = ','.join(options_arr)
date = 'NONE'
show_results = openresults
params = name, options, has_tokens, show_results, question, multi, date
req = 'INSERT INTO {} VALUES (?,?,?,?,?,?,?)'.format(CFG('poll_table_name'))
c.execute(req, params)
tokens = []
if has_tokens:
tokens = genTokens(c, poll_name)
createAdminToken(c, poll_name)
for opt in options_arr:
insertOption(c, poll_name, opt)
closeDB(conn)
return tokens
