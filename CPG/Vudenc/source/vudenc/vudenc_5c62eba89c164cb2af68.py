@inlineCallbacks...
answer = []
answer = yield self.connection.runQuery(query)
print('ERROR: Running query %s' % query)
returnValue(answer)
print(err)
