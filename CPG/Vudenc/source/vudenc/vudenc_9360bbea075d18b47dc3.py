def __init__(self, app_path, name):...
self.name = name
self.path = app_path + '/scripts/' + name
self.exists = file_exists(self.path)
if not self.exists:
return
self.lines = list(self.read_file())
