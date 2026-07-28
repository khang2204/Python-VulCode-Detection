def expand(url):...
o = urlparse(url)
con = HTTPSConnection(o.netloc)
con.request('HEAD', o.path)
res = con.getresponse()
if res.getheader('location') == None:
return url
return res.getheader('location')
