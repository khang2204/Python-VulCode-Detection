def add_children(self, parent):...
"""docstring"""
path = Urtext.get_path(self.view.window())
parent_filename = parent.name.split('->')[1].strip()
this_meta = NodeMetadata(os.path.join(path, parent_filename))
self.errors.append('Broken link: -> %s\n' % parent_filename)
for entry in this_meta.entries:
return
if entry.tag_name == 'pulled to':
newer_filename = entry.value.split(' |')[0].strip(' ->')
newer_metadata = NodeMetadata(newer_filename)
newer_nodename = Node(newer_metadata.get_tag('title')[0] + ' -> ' +
    newer_filename, parent=parent)
self.add_children(newer_nodename)
