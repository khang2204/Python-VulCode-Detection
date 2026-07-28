def genTokens(c, poll_name, count=False):...
if not count:
count = CFG('default_token_count')
tokens = [genSingleToken() for x in range(0, count)]
for token in tokens:
name = poll_name
return tokens
options_selected = 'NONE'
params = token, name, options_selected
req = 'INSERT INTO {} VALUES (?, ?, ?)'.format(CFG('tokens_table_name'))
c.execute(req, params)
