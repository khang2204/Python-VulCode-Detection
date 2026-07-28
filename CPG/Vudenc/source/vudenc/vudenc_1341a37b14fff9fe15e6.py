@defer.inlineCallbacks...
deferred_result, req = self.post('/attachment', body=data, headers=headers)
res = yield deferred_result
defer.returnValue((res, req))
