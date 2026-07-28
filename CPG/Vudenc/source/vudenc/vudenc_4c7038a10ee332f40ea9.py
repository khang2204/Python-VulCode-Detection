def hash_md5_for_file(path):...
"""docstring"""
hash_md5 = hashlib.md5()
for chunk in iter(lambda : f.read(4096), b''):
hash_md5.update(chunk)
path_md5 = hash_md5.hexdigest()
return path_md5
