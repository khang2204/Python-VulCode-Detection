def get_md5_from_file(path):...
"""docstring"""
key_md5 = path + '.md5'
key_md5 = open(key_md5, 'r')
key_md5 = key_md5.read()
return key_md5
