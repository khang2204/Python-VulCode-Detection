def clear(self):...
"""docstring"""
if os.path.exists(self.cache_dir):
shutil.rmtree(self.cache_dir)
