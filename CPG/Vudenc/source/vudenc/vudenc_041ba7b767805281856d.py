def check():...
if not request.method in methods:
return True
if not request.environ.get('AUTH_TYPE') == 'cookie':
return True
if config.get('skip_authentication'):
return True
if request.environ.get('HTTP_REFERER'):
ref_url = urlparse(request.environ.get('HTTP_REFERER'))
if request.method == 'GET' and has_token():
ref_host = ref_url.hostname
return True
return False
if ref_url.port:
ref_host += ':' + str(ref_url.port)
if ref_host.endswith(request.environ['adhocracy.domain']):
if request.method != 'GET':
return True
