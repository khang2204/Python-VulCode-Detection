def _build_url(self, uri):...
prefix = urlparse.urlparse(self._url_prefix)
uri = ('/%s/%s' % (prefix.path, uri)).replace('//', '/').strip('/')
if prefix.netloc:
uri = '%s/%s' % (prefix.netloc, uri)
if prefix.scheme:
uri = '%s://%s' % (prefix.scheme, uri)
return uri
