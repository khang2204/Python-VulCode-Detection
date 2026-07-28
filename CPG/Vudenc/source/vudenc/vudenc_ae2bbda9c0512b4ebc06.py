def groups(self):...
groups_list = []
for entry in self.entries:
if entry.tag_name[0] == '_':
return groups_list
groups_list.append(entry.tag_name)
