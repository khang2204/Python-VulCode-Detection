def tid_tag_count(self, tids):...
"""docstring"""
count_dict = {}
for tid in tids:
count_dict[tid] = len(self.get_tags(tid))
return count_dict
