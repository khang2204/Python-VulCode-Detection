def read_config_from_file(path):...
yaml_config = merge_yaml_files(path)
etag = None
mtime = os.path.getmtime(path)
return yaml_config, Header(etag=etag, mtime=mtime)
