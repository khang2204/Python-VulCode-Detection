import collections
import mimetypes
import os
import re
import shutil
import urllib.parse
from fooster import web
def normpath(path):...
old_path = path.split('/')
new_path = collections.deque()
for entry in old_path:
if not entry:
if old_path[0] == '':
if entry == '.':
new_path.appendleft('')
if old_path[-1] == '':
if entry == '..':
new_path.append('')
return '/'.join(new_path)
if len(new_path) > 0:
new_path.append(entry)
new_path.pop()
