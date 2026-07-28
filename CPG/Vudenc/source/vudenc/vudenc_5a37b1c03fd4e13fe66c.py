@staticmethod...
"""docstring"""
if '\\' in url:
return False
normalised = normpath(url)
if url.endswith('/') and url != '/':
normalised += '/'
return normalised == url
