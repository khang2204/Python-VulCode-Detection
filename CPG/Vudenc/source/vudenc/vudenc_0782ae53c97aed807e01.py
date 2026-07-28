def run(self, edit):...
self.found_tags = []
self.tagged_files = {}
files = Urtext.get_all_files(self.view.window())
for file in files:
if file[-4:] == '.txt':
self.view.window().show_quick_panel(self.found_tags, self.list_files)
metadata = NodeMetadata(os.path.join(Urtext.get_path(self.view.window()), file)
    )
for tag in metadata.get_tag('tags'):
if isinstance(tag, str):
tag = [tag]
for item in tag:
if item not in self.found_tags:
self.found_tags.append(item)
self.tagged_files[item].append(metadata)
self.tagged_files[item] = []
