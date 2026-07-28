def createAdminToken(c, poll_name):...
adm_token = genSingleToken()
params = adm_token, poll_name
req = 'INSERT INTO {} VALUES (?, ?)'.format(CFG('admintoken_table_name'))
c.execute(req, params)
