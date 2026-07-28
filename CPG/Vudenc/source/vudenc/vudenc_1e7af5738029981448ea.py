def get(self, suburl):...
request = urllib2.Request(self.url + suburl)
f = self._opener.open(request)
data = f.read()
return data
