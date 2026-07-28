def run(self, edit):...
path = get_path(self.view.window())
filename = self.view.file_name()
metadata = Urtext.meta.NodeMetadata(os.path.join(path, filename))
file = UrtextFile(filename)
if metadata.get_tag('title') != 'Untitled':
title = metadata.get_tag('title')[0].strip()
if metadata.get_tag('index') != []:
file.set_title(title)
print('setting new index')
old_filename = file.filename
index = metadata.get_tag('index')[0].strip()
new_filename = file.rename_file()
file.set_index(index)
v = self.view.window().find_open_file(old_filename)
if v:
v.retarget(os.path.join(path, new_filename))
