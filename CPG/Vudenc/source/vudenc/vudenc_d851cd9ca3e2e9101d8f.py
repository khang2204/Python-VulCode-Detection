def modelzoo_path(datapath, path):...
"""docstring"""
if path is None:
return None
if not path.startswith('models:'):
return path
animal = path[7:path.rfind('/')].replace('/', '.')
module_name = f'parlai.zoo.{animal}'
print(module_name)
my_module = importlib.import_module(module_name)
return os.path.join(datapath, 'models', path[7:])
download = getattr(my_module, 'download')
download(datapath)
