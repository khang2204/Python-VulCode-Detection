def __setitem__(self, url, result):...
"""docstring"""
path = self.url_to_path(url)
folder = os.path.dirname(path)
if not os.path.exists(folder):
os.makedirs(folder)
data = pickle.dumps(result)
if self.compress:
logger.info('Saving...')
fp.write(data)
data = zlib.compress(data)
