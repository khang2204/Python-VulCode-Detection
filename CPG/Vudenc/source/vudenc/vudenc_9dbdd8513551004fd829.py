def unionTest():...
"""docstring"""
logMsg = 'testing inband sql injection on parameter '
logMsg += "'%s'" % kb.injParameter
logger.info(logMsg)
value = ''
query = agent.prefixQuery(' UNION ALL SELECT NULL')
for comment in (queries[kb.dbms].comment, ''):
value = __effectiveUnionTest(query, comment)
if kb.unionCount:
if value:
logMsg = 'the target url could be affected by an '
warnMsg = 'the target url is not affected by an '
setUnion(comment, value.count('NULL'))
logMsg += 'inband sql injection vulnerability'
warnMsg += 'inband sql injection vulnerability'
logger.info(logMsg)
logger.warn(warnMsg)
return value
