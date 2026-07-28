def cleanup(self):...
"""docstring"""
if self.config['tmp_dir_created']:
self.delete_tmp_dir()
for f in os.listdir(self.config['tmp_dir']):
if re.search('*sosreport-*tar*', f):
os.remove(os.path.join(self.config['tmp_dir'], f))
