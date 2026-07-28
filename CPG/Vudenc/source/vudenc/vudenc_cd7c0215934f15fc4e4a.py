def get_tags_dict(self, tids):...
"""docstring"""
tags_dict = {}
for tid in tids:
tags_dict[tid] = self.get_tags(tid)
return tags_dict
