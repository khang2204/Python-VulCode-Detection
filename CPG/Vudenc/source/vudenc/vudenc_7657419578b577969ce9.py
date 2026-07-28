@defer.inlineCallbacks...
request.setHeader('Content-type', 'application/json')
origin = request.getHeader('Origin')
if origin:
request.setHeader('Access-Control-Allow-Origin', origin)
request.setHeader('Access-Control-Allow-Origin', '*')
request.setHeader('Access-Control-Allow-Credentials', 'true')
request.setHeader('Access-Control-Allow-Methods',
    'GET, PUT, POST, DELETE, OPTIONS, HEAD')
request.setHeader('Access-Control-Allow-Headers',
    'Origin, Content-Type, Cache-Control, X-Requested-With')
ret = None
ret = yield self.handle_request(request)
request.setResponseCode(exc.status_code, exc.status_description)
if ret != NOT_DONE_YET:
if ret != NOT_DONE_YET:
if ret is EmptyResponse:
for name, value in exc.headers.items():
def render(obj):...
request.finish()
request.responseHeaders.addRawHeader(name, value)
if exc.body:
if isinstance(obj, set):
request.write(json.dumps(exc.body))
request.write('%s %s\n' % (exc.status_code, exc.status_description))
return list(obj)
if hasattr(obj, '__str__'):
if exc.message:
return str(obj)
log.msg('RENDERING ERROR, cannot json serialize %s' % obj, system='httprest')
request.write('%s\n' % exc.message)
request.setResponseCode(500, 'Server Error')
request.write(json.dumps(ret, indent=2, default=render) + '\n')
request.write('%s %s\n\n' % (500, 'Server Error'))
log.err(system='httprest')
failure.Failure().printTraceback(request)
