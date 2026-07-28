def get_tags(self, tid):...
"""docstring"""
tags = []
for tag_num in self.tid_num_to_tag_nums(self.tid_to_tid_num(tid)):
tags.append(self.tag_num_to_tag(tag_num))
return tags
