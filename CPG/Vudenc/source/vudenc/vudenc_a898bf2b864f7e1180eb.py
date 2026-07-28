import os
from . import vcstool_clients
def find_repositories(path):...
repos = []
client = get_vcs_client(path)
if client:
repos.append(client)
listdir = os.listdir(path)
listdir = []
for name in listdir:
return repos
subpath = os.path.join(path, name)
if not os.path.isdir(subpath):
repos += find_repositories(subpath)
