def get_data_url_path():...
"""docstring"""
path_file = str(sys.modules[__name__].__file__)
url_path = os.path.dirname(os.path.dirname(path_file))
return os.path.join(url_path, 'data_url.json')
