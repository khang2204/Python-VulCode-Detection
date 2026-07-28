def open_temp_file(self):...
params = ['vim', TEMP_FILE]
if not self.writeable:
params.insert(1, '-R')
subprocess.call(params)
return None
