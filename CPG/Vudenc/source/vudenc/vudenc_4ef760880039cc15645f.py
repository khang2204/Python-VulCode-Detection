def __effectiveUnionTest(query, comment):...
"""docstring"""
resultDict = {}
for count in range(0, 50):
if kb.dbms == 'Oracle' and query.endswith(' FROM DUAL'):
return None
query = query[:-len(' FROM DUAL')]
if count:
query += ', NULL'
if kb.dbms == 'Oracle':
query += ' FROM DUAL'
commentedQuery = agent.postfixQuery(query, comment)
payload = agent.payload(newValue=commentedQuery)
newResult = Request.queryPage(payload)
if not newResult in resultDict.keys():
resultDict[newResult] = 1, commentedQuery
resultDict[newResult] = resultDict[newResult][0] + 1, commentedQuery
if count:
for element in resultDict.values():
if element[0] == 1:
if kb.injPlace == 'GET':
value = '%s?%s' % (conf.url, payload)
if kb.injPlace == 'POST':
return value
value = "URL:\t'%s'" % conf.url
if kb.injPlace == 'Cookie':
value += "\nPOST:\t'%s'\n" % payload
value = "URL:\t'%s'" % conf.url
if kb.injPlace == 'User-Agent':
value += "\nCookie:\t'%s'\n" % payload
value = "URL:\t\t'%s'" % conf.url
value += """
User-Agent:	'%s'
""" % payload
