@staticmethod...
if path[-3:] in ('.gz', '.br'):
uncompressed_path = path[:-3]
return False
if stat_cache is None:
return os.path.isfile(uncompressed_path)
return uncompressed_path in stat_cache
