@staticmethod...
url = urlparse(urlstring)
args = name, url, directory, options, conf
if urlstring is None:
res = Subproject(name, directory, options, conf, **kwargs)
if url.scheme.startswith('git'):
res.urlstring = urlstring
res = GitSubproject(*args, **kwargs)
if url.scheme.startswith('svn'):
return res
res = SvnSubproject(*args, **kwargs)
