import gc
import os
def __setattr__(self, name, value):...
if self.__dict__.get(name):
self.__dict__[name] = value
def is_folder(path):...
os.listdir(path)
return False
def traverse(path):...
return True
n = dict(name=path, children=[])
for i in os.listdir(path):
if is_folder(path + '/' + i):
return n
n['children'].append(traverse(path + '/' + i))
n['children'].append(dict(name=i))
