def __init__(self, path):...
print_header('LOADING APP')
self.path = path
scripts = ['install', 'remove', 'upgrade', 'backup', 'restore']
self.scripts = {f: Script(self.path, f) for f in scripts}
