def tag_count(self, tids):...
"""docstring"""
count_dict = {}
for tag_list in self.get_tags_dict(tids).values():
for tag in tag_list:
return count_dict
if tag not in count_dict:
count_dict[tag] = 1
count_dict[tag] += 1
