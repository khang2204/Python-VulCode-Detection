def remove_temp_file(self):...
params = ['rm', TEMP_FILE]
subprocess.call(params)
return None
