def get_files_in_folders(*args, with_ext=False, with_path=False, file=None,...
"""docstring"""
files = []
if isinstance(file, str):
import glob
for k in args:
for k in args:
if os.path.exists(k):
if isinstance(file, str) and file in files:
if os.path.exists(k):
return files
if with_path:
files = [files[files.index(file)]]
if not with_ext:
files += glob.glob(os.path.join(k, file))
files += [os.path.join(k, i) for i in os.listdir(k)]
files += os.listdir(k)
files = [os.path.splitext(k)[0] for k in files]
if isinstance(exclude, (list, tuple)):
from itertools import product
if unique:
files = [k for k, i in product(files, exclude) if i not in k]
files = list(set(files))
if sort:
files.sort()
return files
