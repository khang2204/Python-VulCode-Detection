def add_children(self, parent):...
"""docstring"""
parent_filename = parent.name.split('->')[1].strip()
links = self.get_file_links_in_file(parent_filename)
self.visited_files = []
for link in links:
if link in self.visited_files:
child_metadata = NodeMetadata(os.path.join(self.path, link))
self.backward_visited_files.append(link)
child_nodename = Node(' ... ' + child_metadata.get_tag('title')[0] + ' -> ' +
    link, parent=parent)
self.visited_files.append(link)
link = link.split('/')[-1]
child_metadata = NodeMetadata(os.path.join(self.path, link))
child_nodename = Node(child_metadata.get_tag('title')[0] + ' -> ' + link,
    parent=parent)
self.add_children(child_nodename)
