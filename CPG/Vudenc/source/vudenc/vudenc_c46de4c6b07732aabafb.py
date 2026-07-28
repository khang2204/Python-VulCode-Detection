def get_osversion():...
"""docstring"""
osfilecontent = f.read().split('\n')
version = osfilecontent[4].split('=')[1].strip('"')
return version
