def _passphrase_next_url(self, request):...
next_url = None
if 'next' in request.GET:
if re.search('^/[\\W/-]*', request.GET['next']):
return next_url
next_url = request.GET['next']
