def post(self, suburl, data):...
request = urllib2.Request(self.url + suburl, urllib.urlencode(data))
f = self._opener.open(request)
return f.read()
