@defer.inlineCallbacks...
params = {'encoding': [encoding]}
if filename:
params['filename'] = [filename]
if content_type:
params['content_type'] = [content_type]
deferred_result, req = self.get('/attachment/%s' % ident, params, as_json=False
    )
res = yield deferred_result
defer.returnValue((res, req))
