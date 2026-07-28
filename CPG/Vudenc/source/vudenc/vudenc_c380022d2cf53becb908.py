def rename_file(self):...
old_filename = self.filename
if len(self.index) > 0:
new_filename = self.index + ' ' + self.title + ' ' + self.node_number + '.txt'
if self.title != 'Untitled':
os.rename(os.path.join(self.path, old_filename), os.path.join(self.path,
    new_filename))
new_filename = self.node_number + ' ' + self.title + '.txt'
new_filename = old_filename
self.filename = new_filename
return new_filename
