def __getitem__(self, url):...
"""docstring"""
path = self.url_to_path(url)
if os.path.exists(path):
data = fp.read()
if self.compress:
logger.info('Loading...')
result = pickle.loads(data)
data = zlib.decompress(data)
return result
