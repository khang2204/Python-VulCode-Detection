def path_to_tmp(file=None, folder=None):...
"""docstring"""
tmp_path = os.path.join(path_to_visbrain_data(), 'tmp')
if not os.path.exists(tmp_path):
os.mkdir(tmp_path)
folder = '' if not isinstance(folder, str) else folder
file = '' if not isinstance(file, str) else file
tmp_path = os.path.join(tmp_path, folder)
if not os.path.exists(tmp_path):
os.mkdir(tmp_path)
return os.path.join(tmp_path, file)
