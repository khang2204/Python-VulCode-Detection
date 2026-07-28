def filter_tags(self, tids, min_tags):...
"""docstring"""
count_dict = self.tid_tag_count(tids)
tids_filtered = [tid for tid in tids if count_dict[tid] >= min_tags]
return tids_filtered
