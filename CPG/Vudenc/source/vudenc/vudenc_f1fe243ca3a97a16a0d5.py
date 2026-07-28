def __delitem__(self, url):...
"""docstring"""
path = self.url_to_path(url)
os.remove(path)
os.removedirs(os.path.dirname(path))
