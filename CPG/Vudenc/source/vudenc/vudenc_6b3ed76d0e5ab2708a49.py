def __init__(self, filename):...
"""docstring"""
super(FileDB, self).__init__()
os.makedirs(path.join(SCRIPT_FOLDER, DATABASES_FOLDER_NAME), exist_ok=True)
self.filename = path.join(SCRIPT_FOLDER, DATABASES_FOLDER_NAME, filename +
    '.db')
self.lock = Lock()
initial = {'type': 0, 'meta': 'str', 'path': 'str', 'mod_time': 0,
    'file_id': 'str'}
if initial:
if path.isfile(self.filename):
for i in initial.keys():
self.createTable(initial)
self._addColumn(i, initial[i])
