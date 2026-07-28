def add_backward_children(self, parent):...
visited_files = []
print(parent)
parent_filename = parent.name.split('->')[1].strip()
print(parent_filename)
links = self.get_links_to_file(parent_filename)
for link in links:
print(link)
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
self.add_backward_children(child_nodename)
